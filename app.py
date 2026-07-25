from mongodb import add_student, view_students, update_student, delete_student
from sqldb import add_enrollment, view_enrollments, update_enrollment, delete_enrollment
from report import reports, export_csv


def show_menu():

    while True:

        print()
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Enrollment")
        print("6. View Enrollments")
        print("7. Update Enrollment")
        print("8. Delete Enrollment")
        print("9. Reports")
        print("10. Export Students to CSV")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            add_enrollment()

        elif choice == "6":
            view_enrollments()

        elif choice == "7":
            update_enrollment()

        elif choice == "8":
            delete_enrollment()

        elif choice == "9":
            reports()

        elif choice == "10":
            export_csv()

        elif choice == "0":
            print("Program Closed")
            break

        else:
            print("Invalid Choice")


show_menu()