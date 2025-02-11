# ======================{ Student Grade System }======================

grades = {}  # Dictionary to store student grades

def get_grade_description(grade):
    """Returns a description based on the grade."""
    grade_dict = {
        "A": "Excellent",
        "B": "Good",
        "C": "Average",
        "D": "Below Average",
        "F": "Fail"
    }
    return grade_dict.get(grade.upper(), "Invalid Grade")

def add_student(name, grade):
    if grade.upper() in ["A", "B", "C", "D", "F"]:
        grades[name] = grade.upper()
        print(f"{name}'s grade ({grade}) added successfully: {get_grade_description(grade)}.")
    else:
        print("Invalid grade! Please enter A, B, C, D, or F.")

def update_student(name, grade):
    if name in grades:
        if grade.upper() in ["A", "B", "C", "D", "F"]:
            grades[name] = grade.upper()
            print(f"{name}'s grade updated successfully: {get_grade_description(grade)}.")
        else:
            print("Invalid grade! Please enter A, B, C, D, or F.")
    else:
        print("Student not found.")

def delete_student(name):
    if name in grades:
        del grades[name]
        print(f"{name}'s grade deleted successfully.")
    else:
        print("Student not found.")

def view_students():
    if grades:
        print("\nStudent Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade} ({get_grade_description(grade)})")
    else:
        print("No students found.")

if __name__ == "__main__":
    while True:
        print("\n1. Add grade")
        print("2. Update grade")
        print("3. Delete grade")
        print("4. View grades")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade (A, B, C, D, F): ")
            add_student(name, grade)

        elif choice == "2":
            name = input("Enter student name: ")
            grade = input("Enter new grade (A, B, C, D, F): ")
            update_student(name, grade)

        elif choice == "3":
            name = input("Enter student name to delete: ")
            delete_student(name)

        elif choice == "4":
            view_students()

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
