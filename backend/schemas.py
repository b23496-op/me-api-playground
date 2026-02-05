from pydantic import BaseModel

class ProfileCreate(BaseModel):
    name: str
    email: str
    education: str
    skills: str
    github: str
    linkedin: str
    portfolio: str


class ProjectCreate(BaseModel):
    title: str
    description: str
    links: str
