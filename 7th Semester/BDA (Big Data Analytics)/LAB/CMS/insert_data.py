import mysql.connector
import random
import string
import time


# Connect to MySQL server
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="#$@#$@",  # the password will be hidden due to security reasons
        database="cms",
    )


# Insert data into the database (more than 1 million records)
def insert_data():
    connection = create_connection()
    cursor = connection.cursor()

    departments = ["CS", "EE", "ME", "CE", "SE"]
    semesters = ["Fall 2023", "Spring 2024", "Fall 2024", "Spring 2025"]
    section_names = ["A", "B", "C", "D"]

    # Insert Departments
    cursor.executemany(
        "INSERT INTO Department (name) VALUES (%s)", [(d,) for d in departments]
    )

    # Insert Semesters
    cursor.executemany(
        "INSERT INTO Semester (name) VALUES (%s)", [(s,) for s in semesters]
    )

    # Insert Teachers, Students, Courses, Sections, and Grades
    for _ in range(1000000):  # Insert 1 million records
        # Randomly generate student, teacher, course, and section data
        dept_id = random.randint(1, 5)
        teacher_name = "".join(random.choices(string.ascii_letters, k=10))
        student_name = "".join(random.choices(string.ascii_letters, k=10))
        course_name = "".join(random.choices(string.ascii_letters, k=8))
        section_name = random.choice(section_names)
        semester_id = random.randint(1, 4)
        grade = round(random.uniform(1.0, 4.0), 2)

        cursor.execute(
            "INSERT INTO Teacher (name, department_id) VALUES (%s, %s)",
            (teacher_name, dept_id),
        )
        teacher_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Student (name, department_id) VALUES (%s, %s)",
            (student_name, dept_id),
        )
        student_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Course (name, department_id, teacher_id) VALUES (%s, %s, %s)",
            (course_name, dept_id, teacher_id),
        )
        course_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Section (name, course_id, semester_id, teacher_id) VALUES (%s, %s, %s, %s)",
            (section_name, course_id, semester_id, teacher_id),
        )
        section_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Grades (student_id, section_id, grade) VALUES (%s, %s, %s)",
            (student_id, section_id, grade),
        )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # create_database_and_tables()
    insert_data()
