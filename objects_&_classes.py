class Robot:
    def introduce_self(self):
        print("My name is ", self.name)
        print(f"I am {self.age} years old")

r1 = Robot()
r1.name = "Tom"
r1.age = 3
r1.color = "red"
r1.weight = 10

r2 = Robot()
r2.name = "Jerry"
r2.age = 2
r2.color = "orange"
r2.weight = 1

r1.introduce_self()
r2.introduce_self()

# -----------------------another method (We will use this new one)

class Robot:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is ", self.name)
        print(f"I am {self.age} years old")

r1 = Robot("Tom", 3, "Red", 8)
r2 = Robot("Jerry", 1, "Orange", 1)

r1.introduce_self()
r2.introduce_self()
