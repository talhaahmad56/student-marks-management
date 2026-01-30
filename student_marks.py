class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  

    def get_marks(self):
        return self._marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
            print(f"Marks updated to {new_marks}")
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def __str__(self):
        return f"Student: {self.name} | Marks: {self._marks}"


# -------- Main Program --------
name = input("Enter student name: ")
marks = int(input("Enter initial marks (0-100): "))

student = Student(name, marks)

while True:
    print("\n1. Show Marks")
    print("2. Update Marks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(student)

    elif choice == "2":
        new_marks = int(input("Enter new marks (0-100): "))
        student.set_marks(new_marks)

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
