class Mammal:
    def eat(self):
        print("eat")
    
    def walk(self):
        print("walk")

class Fish:
    def eat(self):
        print("eat")
    
    def swim(self):
        print("swim")

#Probelm: We have defined eat() TWICE
#Instills: DRY
#Why? if you have a bug, you will have to fix all methods
#Why? if you want to modify, you will have to modify all methods

#Inheritance: mechanism that defines common behavior or funtions in one class
#             Inherit them in other classses  