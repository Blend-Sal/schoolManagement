import re
import sqlite3

onlyNumber = r'^([\s\d]+)$'
onlyLetters = r'^[a-zA-Z]{1}[a-zA-Z]{1}'


def insertStudent(student_id, full_name, age):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, full_name) and re.match(onlyNumber, age):
        conn = sqlite3.connect('school.sqlite')
        cursor = conn.cursor()

        create_table_query = f"INSERT INTO student (StudentID, FullName, Age) VALUES ({student_id}, '{full_name}', {age})"

        cursor.execute(create_table_query)

        conn.commit()
        conn.close()

    else:
        print("Invalid input. Only numbers allowed for ID and Age, and only letters for Full Name.")
