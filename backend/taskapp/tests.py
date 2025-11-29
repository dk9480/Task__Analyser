from django.test import TestCase
from datetime import date, timedelta
from .views import calculate_priority_score

class ScoringAlgorithmTest(TestCase):
    
    def test_urgency_scoring(self):
        """Test that overdue tasks get higher urgency scores"""
        # Test overdue task
        overdue_task = {
            'title': 'Overdue task',
            'due_date': date.today() - timedelta(days=1),  # Yesterday
            'estimated_hours': 5,
            'importance': 5,
            'dependencies': []
        }
        score = calculate_priority_score(overdue_task)
        self.assertGreater(score, 60)  # Adjusted threshold based on your algorithm
        
        # Test task due soon vs task due later
        urgent_task = {
            'title': 'Urgent task',
            'due_date': date.today() + timedelta(days=1),  # Tomorrow
            'estimated_hours': 5,
            'importance': 5,
            'dependencies': []
        }
        
        not_urgent_task = {
            'title': 'Not urgent task',
            'due_date': date.today() + timedelta(days=30),  # Far future
            'estimated_hours': 5,
            'importance': 5,
            'dependencies': []
        }
        
        urgent_score = calculate_priority_score(urgent_task)
        not_urgent_score = calculate_priority_score(not_urgent_task)
        
        # Urgent task should score higher than not urgent task
        self.assertGreater(urgent_score, not_urgent_score)
        
    def test_importance_scoring(self):
        """Test that high importance tasks score well"""
        # High importance task
        important_task = {
            'title': 'Important task',
            'due_date': date.today() + timedelta(days=10),
            'estimated_hours': 5,
            'importance': 9,  # High importance
            'dependencies': []
        }
        important_score = calculate_priority_score(important_task)
        
        # Low importance task
        low_importance_task = {
            'title': 'Low importance task',
            'due_date': date.today() + timedelta(days=10),
            'estimated_hours': 5,
            'importance': 2,  # Low importance
            'dependencies': []
        }
        low_importance_score = calculate_priority_score(low_importance_task)
        
        # High importance should score better
        self.assertGreater(important_score, low_importance_score)
        
    def test_effort_scoring(self):
        """Test that low-effort tasks are preferred in fastest_wins strategy"""
        # Quick task
        quick_task = {
            'title': 'Quick task',
            'due_date': date.today() + timedelta(days=5),
            'estimated_hours': 1,  # Low effort
            'importance': 5,
            'dependencies': []
        }
        
        # Slow task
        slow_task = {
            'title': 'Slow task',
            'due_date': date.today() + timedelta(days=5),
            'estimated_hours': 8,  # High effort
            'importance': 5,
            'dependencies': []
        }
        
        # In fastest_wins strategy, quick task should score higher
        quick_fast_score = calculate_priority_score(quick_task, 'fastest_wins')
        slow_fast_score = calculate_priority_score(slow_task, 'fastest_wins')
        self.assertGreater(quick_fast_score, slow_fast_score)
        
    def test_dependency_scoring(self):
        """Test that tasks with dependencies get higher scores"""
        # Task with dependencies
        task_with_deps = {
            'title': 'Task with dependencies',
            'due_date': date.today() + timedelta(days=7),
            'estimated_hours': 3,
            'importance': 5,
            'dependencies': [1, 2, 3]  # 3 dependencies
        }
        
        # Task without dependencies
        task_no_deps = {
            'title': 'Task without dependencies',
            'due_date': date.today() + timedelta(days=7),
            'estimated_hours': 3,
            'importance': 5,
            'dependencies': []  # No dependencies
        }
        
        deps_score = calculate_priority_score(task_with_deps)
        no_deps_score = calculate_priority_score(task_no_deps)
        
        # Task with dependencies should score higher
        self.assertGreater(deps_score, no_deps_score)
        
    def test_strategy_differences(self):
        """Test that different strategies produce different scores"""
        test_task = {
            'title': 'Test task',
            'due_date': date.today() + timedelta(days=3),
            'estimated_hours': 2,
            'importance': 7,
            'dependencies': [1]
        }
        
        # Get scores for different strategies
        smart_score = calculate_priority_score(test_task, 'smart_balance')
        fast_score = calculate_priority_score(test_task, 'fastest_wins')
        impact_score = calculate_priority_score(test_task, 'high_impact')
        deadline_score = calculate_priority_score(test_task, 'deadline_driven')
        
        # All strategies should produce valid scores
        self.assertGreater(smart_score, 0)
        self.assertGreater(fast_score, 0)
        self.assertGreater(impact_score, 0)
        self.assertGreater(deadline_score, 0)
        
        # At least some scores should be different (they might not all be unique)
        scores = [smart_score, fast_score, impact_score, deadline_score]
        unique_scores = set(scores)
        self.assertGreater(len(unique_scores), 1)  # At least 2 different scores