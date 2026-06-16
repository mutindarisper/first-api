from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, engine
from deps import get_db
from models import Course as CourseModel

app = FastAPI()
Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class CourseCreate(BaseModel):
    name: str
    description: str

@app.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = CourseModel(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()