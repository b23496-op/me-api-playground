from database import SessionLocal
from models import Profile, Project

db = SessionLocal()

# ---- PROFILE ----
p = Profile(
    name="Mulkala Gnaneshwar",
    email="student@example.com",
    education="B.Tech VLSI",
    skills="python, fastapi, verilog, digital design, html, vlsi basics, problem solving",
    github="https://github.com/gnaneshwar",
    linkedin="",
    portfolio=""
)

db.add(p)


# ---- PROJECT 1 ----
pr1 = Project(
    title="Verilog ALU Design",
    description="Designed an 8-bit Arithmetic Logic Unit using Verilog supporting addition, subtraction, logical operations and shift with testbench verification.",
    links="https://github.com/gnaneshwar/alu-verilog"
)

# ---- PROJECT 2 ----
pr2 = Project(
    title="Student Task API",
    description="Simple FastAPI based REST API with SQLite database to manage student tasks with CRUD operations.",
    links="https://github.com/gnaneshwar/task-api"
)

db.add(pr1)
db.add(pr2)

db.commit()

print("seed done with projects")
