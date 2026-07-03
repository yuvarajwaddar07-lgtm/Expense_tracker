# Student Management System

print("Welcome to the student management system ! store your student details here!")

students = []

while True:
    print("\n====MENU====")
    print("1. Add student ")
    print("2. View student details ")
    print("3. Update student details")
    print("4. Delete student details")
    print("5. exit")

    choice = input("\nChoice option:")
    if choice == "1":
        student = {
            "Student ID": input("Enter Student ID:"),
            "Name": input("Enter Student Name:"),
            "Age": int(input("Enter Student Age:")),
            "Class": input("Enter Student Class:"),
            "Department": input("Enter Student Department:"),
            "Email": input("Enter Student Email:"),
            "Grade": input("Enter Student Grade:")
        }
        students.append(student)
        print("Student added successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("No student details available.")
        else:
            for student in students:
                print("\nStudent ID:", student["Student ID"])
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Class:", student["Class"])
                print("Department:", student["Department"])
                print("Email:", student["Email"])
                print("Grade:", student["Grade"])
    elif choice == "3":
        student_id = input("Enter the Student ID to update: ")
        found = False
        for student in students:
            if student["Student ID"] == student_id:
                found = True
                print("Enter new details (leave blank to keep current value):")
                name = input("Enter Student Name (current: {}): ".format(student["Name"]))
                age = input("Enter Student Age (current: {}): ".format(student["Age"]))
                class_name = input("Enter Student Class (current: {}): ".format(student["Class"]))
                department = input("Enter Student Department (current: {}): ".format(student["Department"]))
                email = input("Enter Student Email (current: {}): ".format(student["Email"]))
                grade = input("Enter Student Grade (current: {}): ".format(student["Grade"]))

                if name:
                    student["Name"] = name
                if age:
                    student["Age"] = int(age)
                if class_name:
                    student["Class"] = class_name
                if department:
                    student["Department"] = department
                if email:
                    student["Email"] = email
                if grade:
                    student["Grade"] = grade

                print("Student details updated successfully.")
                break
        if not found:
            print("Student ID not found.")
    elif choice == "4":
        student_id = input("Enter the Student ID to delete: ")
        found = False
        for student in students:
            if student["Student ID"] == student_id:
                found = True
                students.remove(student)
                print("Student details deleted successfully.")
                break
        if not found:
            print("Student ID not found.")
    elif choice == "5":
        print("Exiting from the student management system.")
        break
    else:
        print("Invalid choice. Please try again.")