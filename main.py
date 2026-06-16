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


#lists
countries = ["Kenya", "Seychelles", "Tanzania", "South Africa", "Mauritius"]
print(countries)
#get ranges of items in a list
print(countries[1:]) #outputs ['Seychelles', 'Tanzania', 'South Africa', 'Mauritius']
print(countries[:3]) #outputs ['Kenya', 'Seychelles', 'Tanzania']
print(countries[1:4]) #outputs ['Seychelles', 'Tanzania', 'South Africa']
print(type(countries)) #outputs <class 'list'>

#get the last item in a list
print(countries[-1]) #outputs Mauritius
print(len(countries)) #outputs 5

# joining lists
numbers = [1,2,3,5,5]
languages = ["Python", "JavaScript", "TypeScript"]
numbers.extend(languages) #outputs [1, 2, 3, 5, 5, 'Python', 'JavaScript', 'TypeScript']
print(numbers)

#add an item to the last position of a list
languages.append("Rust")
print(languages) #outputs ['Python', 'JavaScript', 'TypeScript', 'Rust']
print(len(languages)) #outputs 4

#add an item to a specific position in a list
languages.insert(2, "Go")
print(languages) #outputs ['Python', 'JavaScript', 'Go', 'TypeScript', 'Rust']

#remove an item from a list
languages.remove("Go")
print(languages) #outputs ['Python', 'JavaScript', 'TypeScript', 'Rust']

#clear a list
# languages.clear()
# print(languages) #outputs []

#get the index of a particular item in a list
print(languages.index("Rust"))

#get the number of times an item appears in a list
print(languages.count("Rust")) #outputs 1

#arrange items in a list in ascending order
numbers = [5, 3, 1, 4, 2]
numbers.sort()
print(numbers) #outputs [1, 2, 3, 4, 5]

#reverse the order of items in a list
numbers.reverse()
print(numbers) #outputs [5, 4, 3, 2, 1]

languages.reverse()
print(languages) #outputs ['Rust', 'TypeScript', 'JavaScript', 'Python']

#duplicate a list
duplicateLanguages = languages.copy()
print(duplicateLanguages) #outputs ['Rust', 'TypeScript', 'JavaScript', 'Python']

#remove the last item in a list
languages.pop()
print(languages) #outputs ['Rust', 'TypeScript', 'JavaScript']

languages.pop(1)
print(languages) #outputs ['Rust', 'JavaScript']

# del languages[0]
# print(languages) #outputs ['JavaScript']

# del languages
# print(languages) #outputs NameError: name 'languages' is not defined since it is removed entirely



## functions
def greetings():
    print("Hello, welcome to my program!")

greetings()


def greetingsWithName(name:str):
    print(f"Hello {name}, welcome to my program!")


greetingsWithName("Risper")

def addTwoNumbers(num1: int, num2: int):
    return num1 + num2
    print("This will not be printed since it is after the return statement")

print(addTwoNumbers(5, 10)) #outputs 15

#if statements
a = 5
b = 5
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")

dev = True
fullstack = False

if dev and fullstack:
    print("Welcome Risper, the fullstack developer!")
elif dev or fullstack:
    print("Welcome Risper, the developer!")

# #check for odd or even numbers
# number = int(input("Enter a number: "))
# if number%2 == 0:
#     print(f"{number} is an even number")
# else:    
#     print(f"{number} is an odd number")

# #multiples of 5
# number2 = int(input("Enter a seccond number: "))
# if number2%5 == 0:
#     print(f"{number2} is a multiple of 5")
# else:   
#     print(f"{number2} is not a multiple of 5")



#dictionaries
person =  {
    'name': 'Risper',
    'age': 28,
    'country': 'Kenya',
    'developer': 'fullstack'
}

print(person) #outputs {'name': 'Risper', 'age': 28, 'country': 'Kenya', 'developer': 'fullstack'}
print(person['name'])
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}