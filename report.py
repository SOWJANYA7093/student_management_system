from pymongo import MongoClient
import mysql.connector
import pandas as pd


client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ramya@123",
    database="student_management"
)

cursor = connection.cursor()


def reports():

    total_students = collection.count_documents({})

    cursor.execute("SELECT COUNT(*) FROM enrollments")

    total_enrollments = cursor.fetchone()[0]

    cursor.execute("""
    SELECT course_name, COUNT(*)
    FROM enrollments
    GROUP BY course_name
    """)

    courses = cursor.fetchall()

    print()
    print("----------- REPORT -----------")
    print("Total Students :", total_students)
    print("Total Enrollments :", total_enrollments)

    print()
    print("Enrollments Per Course")

    for course in courses:

        print(course[0], ":", course[1])


def export_csv():

    students = list(
        collection.find(
            {},
            {"_id": 0}
        )
    )

    if len(students) == 0:
        print("No Students Found")
        return

    df = pd.DataFrame(students)

    df.to_csv("students.csv", index=False)

    print("Students Exported Successfully")