from pymongo import MongoClient
from validation import validate_email, validate_age

client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]

collection = db["students"]


def add_student():

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    age = input("Enter Student Age: ")

    if not validate_age(age):
        print("Invalid Age")
        return

    age = int(age)

    email = input("Enter Student Email: ")

    if not validate_email(email):
        print("Invalid Email")
        return

    city = input("Enter Student City: ")

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "email": email,
        "city": city
    }

    collection.insert_one(student)

    print("Student Added Successfully")


def view_students():

    students = collection.find()

    found = False

    for student in students:

        found = True

        print()
        print("Student ID :", student["student_id"])
        print("Name :", student["name"])
        print("Age :", student["age"])
        print("Email :", student["email"])
        print("City :", student["city"])

    if found == False:
        print("No Students Found")


def update_student():

    student_id = input("Enter Student ID to Update: ")

    new_name = input("Enter New Name: ")

    new_age = input("Enter New Age: ")

    if not validate_age(new_age):
        print("Invalid Age")
        return

    new_age = int(new_age)

    new_email = input("Enter New Email: ")

    if not validate_email(new_email):
        print("Invalid Email")
        return

    new_city = input("Enter New City: ")

    result = collection.update_one(
        {"student_id": student_id},
        {
            "$set": {
                "name": new_name,
                "age": new_age,
                "email": new_email,
                "city": new_city
            }
        }
    )

    if result.matched_count == 1:
        print("Student Updated Successfully")
    else:
        print("Student ID Not Found")


def delete_student():

    student_id = input("Enter Student ID to Delete: ")

    result = collection.delete_one(
        {"student_id": student_id}
    )

    if result.deleted_count == 1:
        print("Student Deleted Successfully")
    else:
        print("Student ID Not Found")