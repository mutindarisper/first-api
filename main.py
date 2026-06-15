from fastapi import FastAPI
from math import *

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



#numbers in depth: functions
number = 79
print(number)
#get remainnder of a division
print(5%2) #outputs 1

#convert numbers to strings
stringifiedNumber = str(number)
print("number is " + stringifiedNumber) #outputs number is 79 because you can only concatenate strings to strings

#get absolute values
print(abs(-5)) #outputs 5

#get highest value between two numbers
print(max(4, 3.9)) #outputs 4

#get lowest value between two numbers
print(min(4, 3.999)) #outputs 3.999

#round numbers to the nearest integer
print(round(3.5)) #outputs 4
print(round(3.4)) #outputs 3

#binary representation of a number
print(bin(4)) #outputs 0b100

#get math functions from importing the math module
print(sqrt(16)) #outputs 4.0


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}