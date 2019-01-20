class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

#Mammal IS an Animal
class Mammal(Animal):
    def walk(self):
        print("walk")

#Fish IS an Animal
class Fish(Animal):
    def swim(self):
        print("swim")

mammalObj = Mammal()
mammalObj.eat()
print("Age: ", mammalObj.age)

#Probelm: We have defined eat() TWICE
#Instills: DRY
#Why? if you have a bug, you will have to fix all methods
#Why? if you want to modify, you will have to modify all methods

#Inheritance: mechanism that defines common behavior or funtions in one class
#             Inherit them in other classses  