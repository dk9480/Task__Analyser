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


## 📸 Frontend Dashboard Preview
<img width="1900" height="865" alt="image" src="https://github.com/user-attachments/assets/186ebe9c-2558-48ff-aaf5-3964678fdbda" />

### 📊 Smart Balance Results
<img width="1900" height="910" alt="image" src="https://github.com/user-attachments/assets/843f019f-3a81-4b0c-831e-f399866e868a" />

### ⚡ Fastest Wins Strategy
<img width="1899" height="905" alt="image" src="https://github.com/user-attachments/assets/da6cb54c-7913-419e-936b-1760136eda40" />

### 📈 High Impact Results
<img width="1898" height="905" alt="image" src="https://github.com/user-attachments/assets/b553a636-1b31-445d-8a9e-5c826f4dda02" />

### 📅 Deadline Driven Results
<img width="1903" height="909" alt="image" src="https://github.com/user-attachments/assets/23b1ecc2-f133-4f0b-bdf4-904409ae1ed2" />


## 🧠 Algorithm Explanation

The priority scoring algorithm weighs four factors with configurable weights.

---

### 1. **Urgency (40%)**
Based on days until due date.

- Overdue tasks → **100 urgency**
- Formula:  
(30 - days_until_due) / 30 * 100


---

### 2. **Importance (30%)**
User rating scaled from 1–10 → 0–100.

- Formula:  
(importance / 10) * 100


---

### 3. **Effort (20%)**
Lower effort results in a higher score.

- Formula:
(20 - estimated_hours) / 20 * 100


---

### 4. **Dependencies (10%)**
Each dependency adds **+10**, emphasizing critical-path tasks.

---

## 🎯 Sorting Strategies

### **Smart Balance (Default)**
Weights:  
Urgency 40% | Importance 30% | Effort 20% | Dependencies 10%

Best for: **general productivity**

---

### **Fastest Wins**
Weights:  
Effort 60% | Urgency 20% | Importance 20% | Dependencies 10%

Best for: **quick wins**

---

### **High Impact**
Weights:  
Importance 70% | Urgency 20% | Effort 10% | Dependencies 10%

Best for: **strategic goals**

---

### **Deadline Driven**
Weights:  
Urgency 80% | Importance 10% | Effort 10% | Dependencies 10%


## 🏗 Project Structure
```bash
Task__Analyser/
├── backend/
│   ├── manage.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── urls.py
│   └── taskapp/
│       ├── __init__.py
│       ├── views.py
│       ├── urls.py
│       └── tests.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── requirements.txt
└── README.md
```

## 🧪 Running Tests

To execute all backend tests, run:

```bash
cd backend
python manage.py test
```
 - Test Suite Includes
 - Urgency scoring
 - Importance scoring
 - Effort prioritization
 - Dependency scoring
 - Strategy differentiation

## 💡 Design Decisions

### 1. No Database Persistence
- Chose in-memory processing for simplicity and performance  
- Focuses on core algorithm rather than data storage  
- Reduces complexity for this assignment scope  

### 2. Linear Scoring Approach
- Used straightforward linear calculations for clarity  
- Easy to understand, modify, and debug  
- Provides predictable and consistent results  

### 3. Manual CORS Handling
- Implemented CORS headers directly in views  
- Avoids external dependencies  
- Ensures smooth frontend–backend communication  

### 4. Strategy Pattern
- Configurable weighting system demonstrates algorithm flexibility  
- Allows users to adapt to different work contexts  
- Easy to extend with new strategies  

### 5. Comprehensive Error Handling
- Basic validation for task data  
- Circular dependency detection  
- Graceful error responses with user-friendly messages  

---

## ⏱ Time Breakdown

- Backend Development: **2 hours** (API setup, algorithm, endpoints)  
- Frontend Development: **1.5 hours** (UI, API integration, styling)  
- Testing & Debugging: **0.5 hours** (CORS fixes, error handling)  
- Documentation: **0.5 hours** (README, code comments)  
- Unit Tests: **0.5 hours** (test cases for scoring algorithm)  

**Total Development Time: ~5 hours**

---

## 🏆 Bonus Challenges Implemented

### ✅ Unit Tests
- Comprehensive test suite for scoring algorithm  
- Covers all four factors and strategies  
- Ensures algorithm reliability  

### ✅ Multiple Strategies
- Four distinct prioritization approaches  
- Configurable weighting system  
- Demonstrates algorithm flexibility  



## 🔮 Future Improvements

Given more time, I would implement:

- **Database Persistence** for task history and user preferences  
- **Dependency Graph Visualization** to show task relationships  
- **Date Intelligence** considering weekends and holidays in urgency calculation  
- **Eisenhower Matrix View** for visual task categorization  
- **User Authentication** and personalized settings  
- **Machine Learning** for adaptive scoring based on user behavior  
- **Advanced Error Handling** with comprehensive logging  
- **Docker Containerization** for easy deployment  
- **REST API Documentation** with Swagger/OpenAPI  
- **Progressive Web App (PWA) features** for mobile support  


## 👨‍💻 Developer
Last project by D K Vijendra Kumar
