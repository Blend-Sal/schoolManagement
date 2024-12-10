from tkinter import *
import customtkinter as ctk
from school.db_operations import *
import logging
from tkinter import messagebox

#Queries
ifTableNotExist = ("""
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Age INT NOT NULL
    )
""")

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


def create_table_if_not_exists_student():
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