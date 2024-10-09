import mysql.connector
import random
import string
import time


# Connect to MySQL server
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="##$$@#$",  # the password will be hidden due to security reasons
        database="cms",
    )


# Create CMS database and tables
def create_database_and_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS cms")
    cursor.execute("USE cms")

    # Create tables
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Department (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Teacher (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            department_id INT,
            FOREIGN KEY (department_id) REFERENCES Department(id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            department_id INT,
            FOREIGN KEY (department_id) REFERENCES Department(id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Course (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            department_id INT,
            teacher_id INT,
            FOREIGN KEY (department_id) REFERENCES Department(id),
            FOREIGN KEY (teacher_id) REFERENCES Teacher(id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Semester (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Section (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            course_id INT,
            semester_id INT,
            teacher_id INT,
            FOREIGN KEY (course_id) REFERENCES Course(id),
            FOREIGN KEY (semester_id) REFERENCES Semester(id),
            FOREIGN KEY (teacher_id) REFERENCES Teacher(id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Grades (
            student_id INT,
            section_id INT,
            grade DECIMAL(5,2),
            PRIMARY KEY (student_id, section_id),
            FOREIGN KEY (student_id) REFERENCES Student(id),
            FOREIGN KEY (section_id) REFERENCES Section(id)
        )
    """
    )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_database_and_tables()
