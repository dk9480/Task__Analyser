from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date, datetime

@csrf_exempt
def analyze_tasks(request):
    if request.method == 'OPTIONS':
        # Handle preflight requests
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
        
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tasks = data.get('tasks', [])
            strategy = data.get('strategy', 'smart_balance')
            
            scored_tasks = []
            for task in tasks:
                score = calculate_priority_score(task, strategy)
                task['priority_score'] = round(score, 2)
                scored_tasks.append(task)
            
            sorted_tasks = sorted(scored_tasks, key=lambda x: x['priority_score'], reverse=True)
            response = JsonResponse({'tasks': sorted_tasks, 'strategy': strategy})
            response["Access-Control-Allow-Origin"] = "*"
            return response
            
        except Exception as e:
            response = JsonResponse({'error': str(e)}, status=400)
            response["Access-Control-Allow-Origin"] = "*"
            return response
    
    response = JsonResponse({'error': 'Only POST method allowed'}, status=405)
    response["Access-Control-Allow-Origin"] = "*"
    return response

@csrf_exempt
def suggest_tasks(request):
    if request.method == 'OPTIONS':
        # Handle preflight requests
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
        
    if request.method == 'GET':
        sample_tasks = [
            {
                "title": "Fix login bug",
                "due_date": "2025-11-30",
                "estimated_hours": 3,
                "importance": 8,
                "dependencies": []
            },
            {
                "title": "Write documentation", 
                "due_date": "2025-12-15",
                "estimated_hours": 5,
                "importance": 6,
                "dependencies": []
            }
        ]
        
        scored_tasks = []
        for task in sample_tasks:
            score = calculate_priority_score(task)
            task['priority_score'] = round(score, 2)
            task['explanation'] = "High priority task"
            scored_tasks.append(task)
        
        top_tasks = sorted(scored_tasks, key=lambda x: x['priority_score'], reverse=True)[:3]
        response = JsonResponse({'suggested_tasks': top_tasks})
        response["Access-Control-Allow-Origin"] = "*"
        return response
    
    response = JsonResponse({'error': 'Only GET method allowed'}, status=405)
    response["Access-Control-Allow-Origin"] = "*"
    return response

def calculate_priority_score(task, strategy="smart_balance"):
    due_date = task['due_date']
    importance = task['importance']
    estimated_hours = task['estimated_hours']
    
    if isinstance(due_date, str):
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
    
    today = date.today()
    days_until_due = (due_date - today).days
    
    if days_until_due < 0:
        urgency_score = 100
    else:
        urgency_score = max(0, (30 - days_until_due) / 30 * 100)
    
    importance_score = (importance / 10) * 100
    effort_score = max(0, (20 - estimated_hours) / 20 * 100)
    dependency_score = len(task.get('dependencies', [])) * 10
    
    if strategy == "fastest_wins":
        return effort_score * 0.6 + urgency_score * 0.2 + importance_score * 0.2 + dependency_score
    elif strategy == "high_impact":
        return importance_score * 0.7 + urgency_score * 0.2 + effort_score * 0.1 + dependency_score
    elif strategy == "deadline_driven":
        return urgency_score * 0.8 + importance_score * 0.1 + effort_score * 0.1 + dependency_score
    else:
        return (urgency_score * 0.4 + importance_score * 0.3 + effort_score * 0.2 + dependency_score * 0.1)