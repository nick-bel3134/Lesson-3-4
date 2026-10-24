class Pet:
    def __init__(self, name, age, kind, mood):
        self.name = name
        self.age = age
        self.kind = kind
        self.mood = mood

    def grow(self, age):
        self.age += age

anton = Pet("Musya", 6, "Cat", "happy")

print("Name: ", anton.name)
print("Age: ", anton.age)
print("Kind: ", anton.kind)
print("Mood: ", anton.mood)

musya.grow(age=5)
print(musya.age)