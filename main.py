from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, engine
from deps import get_db
from models import Course as CourseModel
from Enemy import *

app = FastAPI()
#Base.metadata.create_all(bind=engine)
vampire = Enemy(" Vampire", 400, 1000)
vampire.get_type_of_enemy()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class CourseCreate(BaseModel):
    name: str
    description: str

vampire.talk()
vampire.walk_forward()
vampire.attack()
print(f' {vampire.get_type_of_enemy()} has {vampire.health_points} healthpoints and can do attack of {vampire.attack_damage}')


ogre = Ogre(10, 1)
print(ogre.spread_disease())

#polymorphism

def battle(e: Enemy):
    e.talk()
    e.attack()

ogre2 = Ogre(100, 1000)

battle(ogre2)




# @app.post("/courses")
# def create_course(course: CourseCreate, db: Session = Depends(get_db)):
#     db_course = CourseModel(**course.model_dump())
#     db.add(db_course)
#     db.commit()
#     db.refresh(db_course)
#     return db_course

# @app.get("/courses")
# def get_courses(db: Session = Depends(get_db)):
#     return db.query(CourseModel).all()