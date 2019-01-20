class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Mammal IS an Animal


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 14

    def walk(self):
        print("walk")

# Fish IS an Animal


class Fish(Animal):
    def swim(self):
        print("swim")


mammalObj = Mammal()
mammalObj.eat()
print("Age: ", mammalObj.age)
print("Weight: ", mammalObj.weight)

# Probelm: We have defined eat() TWICE
#Instills: DRY
# Why? if you have a bug, you will have to fix all methods
# Why? if you want to modify, you will have to modify all methods

# Inheritance: mechanism that defines common behavior or funtions in one class
#             Inherit them in other classses
#
# Object Class: Mammal isInstanceOf Animal and Animal isInstanceOf Object
# i.e. Mammal isInstanceOf Object
#
# CAUTION: Too much Inheritance is BAD. Increases Complexity.
# Side note: PASS Class
#
# AVOID mullti-level Inheritance such as an Employee - is a Person - is a Living Being - is a Thing.
# Stick to solving business problem in real world

# CAUTION: Multiple Inheritance - class Manager(Employee, Person) has a different behavior
#                           than class Manager(Person, Employee)
#  This can be done by other DEVs on the team
