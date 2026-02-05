from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Profile, Project
from schemas import ProfileCreate, ProjectCreate

app = FastAPI()

# ---- CORS ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- SERVE FRONTEND ----
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

Base.metadata.create_all(bind=engine)



# -------- HEALTH ENDPOINT --------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------- PROFILE CREATE --------
@app.post("/profile")
def create_profile(data: ProfileCreate, db: Session = Depends(get_db)):
    p = Profile(**data.dict())
    db.add(p)
    db.commit()
    return {"message": "profile saved"}


# -------- GET PROFILE --------
@app.get("/profile")
def get_profile(db: Session = Depends(get_db)):
    return db.query(Profile).first()


# -------- ADD PROJECT --------
@app.post("/projects")
def add_project(data: ProjectCreate, db: Session = Depends(get_db)):
    pr = Project(**data.dict())
    db.add(pr)
    db.commit()
    return {"message": "project added"}


# -------- LIST PROJECTS --------
@app.get("/projects")
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


# -------- SEARCH SKILL --------
@app.get("/skills")
def search(skill: str, db: Session = Depends(get_db)):
    p = db.query(Profile).first()

    if not p:
        return []

    if skill.lower() in p.skills.lower():
        return [skill]
    return []
