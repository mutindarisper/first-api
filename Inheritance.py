class Animal:
    weight: int
    color: str
    age: int
    animal_type: str

    def eat(self):
        print(f" I am eating")

    def sleep(self):
        print(f" I am sleeping")



class Dog(Animal):
    can_shed: bool
    domestic_name: str


    def bark(self):
        print(f" Woof Woof")

    def eat(self):
        print("dog eating")

dog = Dog()

print(dog.eat())

