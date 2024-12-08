import mysql.connector
import re
from tkinter import messagebox
import logging

# Regular expressions for validation
onlyNumber = r'^\d+$'
onlyLetters = r'^[a-zA-Z\s]+$'
onlyAge = r'^\d+$'

# Queries
ifTableNotExist = ("""
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Age INT NOT NULL
    )
""")
insertStudentQuery = "INSERT INTO Students (StudentID, Name, Age) VALUES (%s, %s, %s)"
deleteStudentQuery = "DELETE FROM Students WHERE StudentID = %s AND Name = %s AND Age = %s"
updateStudentQuery = "UPDATE Students SET Name = %s WHERE StudentID = %s"

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def connect_to_server():
    """Establish a connection to the MySQL server."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root'
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to MySQL server: {err}")
        logging.error(f"Error connecting to MySQL server: {err}")
        return None


def ensure_database_exists():
    """Ensure the `school` database exists."""
    conn = connect_to_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS school")
            conn.commit()
        except mysql.connector.Error as err:
            logging.error(f"Error creating database: {err}")
            messagebox.showerror("Error", f"Error creating database: {err}")
        finally:
            cursor.close()
            conn.close()


def connect_db():
    """Establish a connection to the `school` database."""
    ensure_database_exists()  # Ensure the database exists before connecting
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='school',
            port=3306
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to MySQL: {err}")
        logging.error(f"Error connecting to MySQL: {err}")
        return None


def create_table_if_not_exists():
    """Ensure the Students table exists in the database."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(ifTableNotExist)
            conn.commit()
        except mysql.connector.Error as err:
            logging.error(f"Error creating the table: {err}")
            messagebox.showerror("Error", f"Error creating the table: {err}")
        finally:
            cursor.close()
            conn.close()


def validate_input(student_id, full_name=None, age=None):
    """Validate student input data."""
    if not re.match(onlyNumber, student_id):
        messagebox.showerror("Invalid Input", "Student ID must be numeric.")
        return False
    if not re.match(onlyLetters, full_name):
        messagebox.showerror("Invalid Input", "Name must contain only letters and spaces.")
        return False
    if not re.match(onlyAge, age):
        messagebox.showerror("Invalid Input", "Age must be numeric.")
        return False
    return True


def execute_query(query, params):
    """Execute a query and return the cursor rowcount."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount
        except mysql.connector.Error as err:
            logging.error(f"Query Execution Error: {err}")
            messagebox.showerror("Database Error", f"An error occurred: {err}")
            return None
        finally:
            cursor.close()
            conn.close()
    return None


def insertStudent(student_id, full_name, age):
    """Insert a new student into the database."""
    if validate_input(student_id, full_name, age):
        create_table_if_not_exists()
        rowcount = execute_query(insertStudentQuery, (int(student_id), full_name, int(age)))
        if rowcount:
            messagebox.showinfo("Success", "Student successfully added to the database.")
        else:
            messagebox.showerror("Error", "An error occurred while adding the student.")


def deleteStudent(student_id, full_name, age):
    """Delete a student from the database."""
    if validate_input(student_id, full_name, age):
        rowcount = execute_query(deleteStudentQuery, (int(student_id), full_name, int(age)))
        if rowcount > 0:
            messagebox.showinfo("Success", "Student successfully deleted from the database.")
        else:
            messagebox.showinfo("Not Found", "No student found with the given ID, Name, and Age.")


def updateStudent(student_id, new_name):
    """Update a student's name in the database."""
    if validate_input(student_id, full_name=new_name):
        rowcount = execute_query(updateStudentQuery, (new_name, int(student_id)))
        if rowcount > 0:
            messagebox.showinfo("Success", "Student successfully updated in the database.")
        else:
            messagebox.showinfo("Not Found", "No student found with the given ID.")
