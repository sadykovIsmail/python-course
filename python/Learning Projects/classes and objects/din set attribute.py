class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)

attr = input("Enter attribute name to change (name or age): ")
value = input("Enter new value: ")

setattr(p, attr, value)  # ✅ Dynamically sets the attribute
print(f"{attr} updated to:", getattr(p, attr))
