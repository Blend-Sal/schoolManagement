import re
import sqlite3

onlyNumber = r'^([\s\d]+)$'

tableCreator = (
    "CREATE TABLE [IF NOT EXISTS] [school].student (StudentID INT PRIMARY KEY NOT NULL, FullName VARCHAR( "
    "NOT NULL, Age INT NOT NULL DEFAULT 0,table_constraints) [WITHOUT ROWID];")


def create_table(student_id, full_name, age):
    if re.match(onlyNumber, student_id):

        conn = sqlite3.connect('school.sqlite')
        cursor = conn.cursor()

        create_table_query = tableCreator

        cursor.execute(create_table_query)

        conn.commit()
        conn.close()

    else:
        print("Only numbers allowed")

