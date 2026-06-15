from fastapi import FastAPI

# variables
name = "Risper"
age = 28

print(f"{name} is {age}!")
print(name, "is", age, "years old.")

#strings in depth: functions
print("Hi. \nHow are you")
print(name[0])
#outputs R

print(name.upper()) #outputs RISPER
print(name.lower()) #outputs risper
print(name.capitalize()) #outputs Risper
print(name.title()) #outputs Risper

#check if all characters are lowercase 
print(name.islower()) #outputs False

#check if all characters are uppercase 
print(name.isupper()) #outputs False

#combine functions
print(name.upper().isupper()) #outputs True

#check number of characters
print(len(name)) #outputs 6

#find the position/index of a character in a string
print(name.index("p")) #outputs 3

#replace a character in a string
print(name.replace("r", "s")) #outputs Rispes





app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}