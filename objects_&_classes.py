class Robot:
    def introduce_self(self):
        print("My name is ", self.name)
        print(f"I am {self.age} years old")

r1 = Robot()
r1.name = "Tom"
r1.age = 3
r1.color = "red"
r1.weight = 10

r1.introduce_self()
