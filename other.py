class Pet:
    def __init__(self, name, age, kind, mood):
        self.name = name
        self.age = age
        self.kind = kind
        self.mood = mood

    def grow(self, age):
        self.age += age

barsyk = Pet("Barsyk", 6, "Cat", "happy")

print("Name: ", barsyk.name)
print("Age: ", barsyk.age)
print("Kind: ", barsyk.kind)
print("Mood: ", barsyk.mood)

barsyk.grow(age=5)
print(barsyk.age)