class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("BARK")

class Cat:
    def meow(self):
        print("MEOW")

dog=Dog()
dog.bark()
dog.walk()