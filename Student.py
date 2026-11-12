
students = []

def add_student():
    name = input("Enter student name: ")

    marks1 = float(input("Enter Python marks: "))
    marks2 = float(input("Enter Maths marks: "))
    marks3 = float(input("Enter Physics marks: "))

    total = marks1 + marks2 + marks3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    student = {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records available")
    else:
        for i, student in enumerate(students, 1):
            print("Student:", i)
            print("Name:", student["name"])
            print("Total:", student["total"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])
            print("-------------------")

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
      
