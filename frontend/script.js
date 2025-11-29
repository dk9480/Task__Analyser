// Strategy button functionality
function setupStrategyButtons() {
    const strategyBtns = document.querySelectorAll('.strategy-btn');
    const strategySelect = document.getElementById('strategy');
    
    strategyBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            strategyBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            // Update hidden select value
            strategySelect.value = this.dataset.strategy;
        });
    });
}

async function analyzeTasks() {
    const jsonInput = document.getElementById('jsonInput').value;
    const strategy = document.getElementById('strategy').value;
    const resultsDiv = document.getElementById('results');
    
    if (!jsonInput) {
        resultsDiv.innerHTML = '<div class="error-message">⚠️ Please enter tasks in JSON format</div>';
        return;
    }
    
    try {
        const tasks = JSON.parse(jsonInput);
        
        // Show loading state
        resultsDiv.innerHTML = '<div class="loading">Analyzing your tasks</div>';
        
        const response = await fetch('http://127.0.0.1:8000/api/tasks/analyze/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                tasks: tasks,
                strategy: strategy
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }
        
        displayResults(data.tasks);
        
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error-message">❌ Error: ${error.message}</div>`;
    }
}

async function getSuggestions() {
    const suggestionsDiv = document.getElementById('suggestions');
    
    try {
        // Show loading state
        suggestionsDiv.innerHTML = '<div class="loading">Getting smart suggestions</div>';
        
        const response = await fetch('http://127.0.0.1:8000/api/tasks/suggest/');
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to get suggestions');
        }
        
        displaySuggestions(data.suggested_tasks);
        
    } catch (error) {
        suggestionsDiv.innerHTML = `<div class="error-message">❌ Error: ${error.message}</div>`;
    }
}

function displayResults(tasks) {
    const resultsDiv = document.getElementById('results');
    
    if (tasks.length === 0) {
        resultsDiv.innerHTML = '<div class="error-message">No tasks to display</div>';
        return;
    }
    
    let html = '';
    tasks.forEach((task, index) => {
        const priorityClass = getPriorityClass(task.priority_score);
        const rankEmoji = getRankEmoji(index);
        
        html += `
            <div class="task-card ${priorityClass}">
                <div class="task-header">
                    <div class="task-title">
                        ${rankEmoji} ${task.title}
                    </div>
                    <div class="priority-score">
                        ${task.priority_score}
                    </div>
                </div>
                <div class="task-details">
                    <div class="detail-item">
                        <span class="detail-label">📅 Due Date</span>
                        <span class="detail-value">${task.due_date}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">⏱️ Effort</span>
                        <span class="detail-value">${task.estimated_hours} hours</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">⭐ Importance</span>
                        <span class="detail-value">${task.importance}/10</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">🔗 Dependencies</span>
                        <span class="detail-value">${task.dependencies.length} tasks</span>
                    </div>
                </div>
            </div>
        `;
    });
    
    resultsDiv.innerHTML = html;
}

function displaySuggestions(tasks) {
    const suggestionsDiv = document.getElementById('suggestions');
    
    if (tasks.length === 0) {
        suggestionsDiv.innerHTML = '<div class="error-message">No suggestions available</div>';
        return;
    }
    
    let html = '';
    tasks.forEach((task, index) => {
        const priorityClass = getPriorityClass(task.priority_score);
        const rankEmoji = ['🥇', '🥈', '🥉'][index] || '🎯';
        
        html += `
            <div class="task-card ${priorityClass}">
                <div class="task-header">
                    <div class="task-title">
                        ${rankEmoji} ${task.title}
                    </div>
                    <div class="priority-score">
                        ${task.priority_score}
                    </div>
                </div>
                <div class="task-details">
                    <div class="detail-item">
                        <span class="detail-label">📅 Due Date</span>
                        <span class="detail-value">${task.due_date}</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">⏱️ Effort</span>
                        <span class="detail-value">${task.estimated_hours} hours</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">⭐ Importance</span>
                        <span class="detail-value">${task.importance}/10</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">💡 Why</span>
                        <span class="detail-value">${task.explanation}</span>
                    </div>
                </div>
            </div>
        `;
    });
    
    suggestionsDiv.innerHTML = html;
}

function getPriorityClass(score) {
    if (score >= 70) return 'high-priority';
    if (score >= 40) return 'medium-priority';
    return 'low-priority';
}

function getRankEmoji(index) {
    const emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'];
    return emojis[index] || '📌';
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    setupStrategyButtons();

});
