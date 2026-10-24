class Student:
    def __init__(self, name, age, height, number):
        self.name = name
        self.age = age
        self.height = height
        self.number = number

    def grow(self, height):
        self.height += height


anton = Student("Anton", 12, 166, 383838383838)

print("Name: ", anton.name)
print("Age: ", anton.age)
print("Height: ", anton.height)
print("Number: ", anton.number)

anton.grow(height=5)
print(anton.height)