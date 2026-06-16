from fastapi import FastAPI
from pydantic import BaseModel
  
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class Course(BaseModel):
    id: int
    name: str
    description: str
    lesson_count: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name" : item.name, "item_price": item.price, "item_id": item_id}

@app.get("/courses", response_model=list[Course])
def read_courses():
    return [
        Course(
            id=1,
            name="Python",
            description="Learn Python fundamentals.",
            lesson_count=12
        ),
        Course(
            id=2,
            name="Javascript",
            description="Learn JavaScript fundamentals.",
            lesson_count=15
        )
    ]