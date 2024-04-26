import sqlite3
import re
from tkinter import messagebox

onlyNumber = r'^\d+$'
onlyLetters = r'^[a-zA-Z]+$'
onlyAge = r'^\d+$'


def insertStudent(student_id, full_name, age):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, full_name) and re.match(onlyAge, age):
        try:
            with sqlite3.connect('school.sqlite') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO student (StudentID, FullName, Age) VALUES (?, ?, ?)",
                               (student_id, full_name, age))
                conn.commit()
                messagebox.showinfo("Success", "Student successfully added to the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            messagebox.showerror("Error", "An error occurred while adding the student to the database.")
    else:
        print("Invalid input. Only numbers allowed for ID and Age, and only letters for Full Name.")
        messagebox.showerror("Invalid Input", "Please enter valid data.")

