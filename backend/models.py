from sqlalchemy import Column, Integer, String, Text
from database import Base

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    education = Column(String)
    skills = Column(Text)
    github = Column(String)
    linkedin = Column(String)
    portfolio = Column(String)


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    links = Column(String)
    