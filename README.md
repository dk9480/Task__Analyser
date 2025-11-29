# 🚀 Smart Task Analyzer

A Django-based application that intelligently scores and prioritizes tasks based on multiple factors.  
This project helps users identify which tasks they should work on first using a sophisticated priority scoring algorithm.

<img width="1901" height="886" alt="image" src="https://github.com/user-attachments/assets/e4dc4750-1182-4077-a78c-a6700aa3fd19" />


---

## ✨ Features

- **4 Sorting Strategies:** Smart Balance, Fastest Wins, High Impact, Deadline Driven  
- **REST API** with CORS support  
- **Responsive Frontend** with real-time task analysis  
- **Priority Scoring Algorithm** considering urgency, importance, effort, and dependencies  
- **Unit Tests** for comprehensive algorithm testing  

---

## 🛠 Tech Stack

**Backend:** Django 4.2, Django REST Framework  
**Frontend:** Vanilla JavaScript, HTML5, CSS3  
**Database:** SQLite  
**Testing:** Django Test Framework  

---

## 📋 Prerequisites

- Python 3.8+
- pip package manager

---

## 🚀 Installation & Setup

### 1. Clone and Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd Task__Analyser

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 3. Run the Backend Server
```bash
cd backend
python manage.py runserver
```
The backend will start at:
http://127.0.0.1:8000/

## 4. Install Dependencies
    #Navigate to the frontend/ folder
    #Open index.html in your web browser

## 📡 API Endpoints
### POST /api/tasks/analyze/
    Analyze and prioritize a list of tasks.
<img width="1470" height="847" alt="image" src="https://github.com/user-attachments/assets/61ab64cb-2bd2-4093-b6b6-5d3dbb4e2554" />

### GET /api/tasks/suggest/  
    Get top 3 task suggestions.
<img width="1478" height="882" alt="image" src="https://github.com/user-attachments/assets/134afdff-ae84-4a3c-80b3-6a4ac172ed15" />



