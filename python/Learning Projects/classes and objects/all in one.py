class Student:
    def __init__(self, name):
        self.name = name

def main():
    student = Student("John")

    while True:
        print("\n--- Student Attribute Manager ---")
        print("1. Add / Update attribute")
        print("2. View attribute")
        print("3. Delete attribute")
        print("4. Check if attribute exists")
        print("5. Show all attributes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            attr = input("Enter attribute name: ")
            value = input("Enter attribute value: ")
            setattr(student, attr, value)
            print(f"✅ Attribute '{attr}' set to '{value}'.")

        elif choice == "2":
            attr = input("Enter attribute name to view: ")
            if hasattr(student, attr):
                print(f"🔍 {attr} =", getattr(student, attr))
            else:
                print(f"❌ '{attr}' not found.")

        elif choice == "3":
            attr = input("Enter attribute name to delete: ")
            if hasattr(student, attr):
                delattr(student, attr)
                print(f"🗑️ '{attr}' deleted.")
            else:
                print(f"❌ '{attr}' does not exist.")

        elif choice == "4":
            attr = input("Enter attribute name to check: ")
            if hasattr(student, attr):
                print(f"✅ '{attr}' exists.")
            else:
                print(f"❌ '{attr}' does not exist.")

        elif choice == "5":
            print("📋 Current attributes:", student.__dict__)

        elif choice == "6":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.")

main()
