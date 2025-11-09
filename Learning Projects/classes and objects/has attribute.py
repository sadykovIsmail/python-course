class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 25)

attr = input("Enter attribute name to check: ")

if hasattr(p, attr):
    print(f"✅ Attribute '{attr}' exists! Its value is:", getattr(p, attr))
else:
    print(f"❌ Attribute '{attr}' does not exist.")
