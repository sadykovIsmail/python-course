class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 25)

attr = input("Enter attribute name to delete: ")

if hasattr(p, attr):
    delattr(p, attr)
    print(f"🗑️ Attribute '{attr}' deleted successfully!")
else:
    print(f"❌ Attribute '{attr}' not found.")
