class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
class Cat(Pet):
    def speak(self):
        print("Miau")

class Dog(Pet):
    def speak(self):
        print("Ham")
class Fish(Pet):
    pass
f = Fish("Pete",3)

p = Pet("Iuli",14)
p.show()
c= Cat("Maria",13)
c.show()
d= Dog("Dogo",13)
d.show()
c.speak()
d.speak()
