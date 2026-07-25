import mysql.connector
from validation import validate_date

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ramya@123",
    database="student_management"
)

cursor = connection.cursor()


def add_enrollment():

    student_id = input("Enter Student ID: ")

    course_name = input("Enter Course Name: ")

    enrollment_date = input("Enter Enrollment Date (YYYY-MM-DD): ")

    if not validate_date(enrollment_date):
        print("Invalid Date Format")
        return

    query = """
    INSERT INTO enrollments(student_id, course_name, enrollment_date)
    VALUES(%s,%s,%s)
    """

    values = (
        student_id,
        course_name,
        enrollment_date
    )

    cursor.execute(query, values)

    connection.commit()

    print("Enrollment Added Successfully")


def view_enrollments():

    cursor.execute("SELECT * FROM enrollments")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No Enrollments Found")

    else:

        for row in rows:

            print()
            print("Enrollment ID :", row[0])
            print("Student ID :", row[1])
            print("Course Name :", row[2])
            print("Enrollment Date :", row[3])


def update_enrollment():

    enrollment_id = input("Enter Enrollment ID: ")

    student_id = input("Enter New Student ID: ")

    course_name = input("Enter New Course Name: ")

    enrollment_date = input("Enter New Date (YYYY-MM-DD): ")

    if not validate_date(enrollment_date):
        print("Invalid Date Format")
        return

    query = """
    UPDATE enrollments
    SET student_id=%s,
        course_name=%s,
        enrollment_date=%s
    WHERE enrollment_id=%s
    """

    values = (
        student_id,
        course_name,
        enrollment_date,
        enrollment_id
    )

    cursor.execute(query, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("Enrollment Updated Successfully")
    else:
        print("Enrollment ID Not Found")


def delete_enrollment():

    enrollment_id = input("Enter Enrollment ID to Delete: ")

    query = """
    DELETE FROM enrollments
    WHERE enrollment_id=%s
    """

    cursor.execute(query, (enrollment_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Enrollment Deleted Successfully")
    else:
        print("Enrollment ID Not Found")