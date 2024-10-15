import mysql.connector
import re
from tkinter import messagebox

onlyNumber = r'^\d+$'
onlyLetters = r'^[a-zA-Z\s]+$'
onlyAge = r'^\d+$'

ifTablenotExist = ("""
            CREATE TABLE IF NOT EXISTS Students (
                StudentID INT PRIMARY KEY,
                Name VARCHAR(255) NOT NULL,
                Age INT NOT NULL
            )
        """)

insertStudentQuery = "INSERT INTO Students (StudentID, Name, Age) VALUES (%s, %s, %s)"
deleteStudentQuery = "DELETE FROM Students WHERE StudentID = %s AND Name = %s AND Age = %s"
updateStudentQuery = "UPDATE Students SET Name = %s WHERE StudentID = %s"


def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            database='school'
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to MySQL: {err}")
        return None


def create_table_if_not_exists(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(ifTablenotExist)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"An error occurred while creating the table: {err}")
        messagebox.showerror("Error", f"An error occurred while ensuring the table exists: {err}")


def insertStudent(student_id, full_name, age):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, full_name) and re.match(onlyAge, age):
        conn = connect_db()
        if conn:
            try:
                create_table_if_not_exists(conn)  # Ensure table exists before insertion
                cursor = conn.cursor()
                cursor.execute(insertStudentQuery, (student_id, full_name, age))
                conn.commit()
                messagebox.showinfo("Success", "Student successfully added to the database.")
            except mysql.connector.Error as err:
                print(f"An error occurred: {err}")
                messagebox.showerror("Error", f"An error occurred while adding the student: {err}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Database connection failed.")
    else:
        print("Invalid input. Only numbers allowed for ID and Age, and only letters for Full Name.")
        messagebox.showerror("Invalid Input", "Please enter valid data.")


def deleteStudent(student_id, full_name, age):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, full_name) and re.match(onlyAge, age):
        conn = connect_db()
        if conn:
            try:
                create_table_if_not_exists(conn)  # Ensure table exists before deletion
                cursor = conn.cursor()
                cursor.execute(deleteStudentQuery, (student_id, full_name, age))
                conn.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Student successfully deleted from the database.")
                else:
                    messagebox.showinfo("Not Found", "No student found with the given ID, Name, and Age.")
            except mysql.connector.Error as err:
                print(f"An error occurred: {err}")
                messagebox.showerror("Error", f"An error occurred while deleting the student: {err}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Database connection failed.")
    else:
        print("Invalid input. Only numbers allowed for ID and Age, and only letters and spaces for Full Name.")
        messagebox.showerror("Invalid Input", "Please enter valid data for ID, Name, and Age.")


def updateStudent(student_id, new_name):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, new_name):
        conn = connect_db()
        if conn:
            try:
                create_table_if_not_exists(conn)  # Ensure table exists before update
                cursor = conn.cursor()
                cursor.execute(insertStudentQuery, (new_name, student_id))
                conn.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Student successfully updated in the database.")
                else:
                    messagebox.showinfo("Not Found", "No student found with the given ID.")
            except mysql.connector.Error as err:
                print(f"An error occurred: {err}")
                messagebox.showerror("Error", f"An error occurred while updating the student: {err}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Database connection failed.")
    else:
        print("Invalid input. Only numbers allowed for ID and only letters for Full Name.")
        messagebox.showerror("Invalid Input", "Please enter valid data.")
