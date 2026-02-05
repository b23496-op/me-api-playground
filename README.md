# Me API Playground

A simple full-stack portfolio API that exposes my profile and projects using FastAPI backend and HTML frontend.

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
- HTML + JavaScript

## Features
- Get profile information  
- List projects  
- Search skills  
- REST API design  
- Database integration  

## How to Run

### Backend
cd backend
pip install -r requirements.txt
python seed.py
python -m uvicorn main:app --reload


### Frontend
cd frontend
python -m http.server 5500


Open:  
http://localhost:5500


## API Endpoints

GET /profile  
GET /projects  
GET /skills?skill=python  
GET /health  

## Author
Mulkala Gnaneshwar  
B.Tech VLSI Student
