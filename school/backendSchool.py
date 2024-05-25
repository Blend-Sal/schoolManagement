import sqlite3
import re
from tkinter import messagebox

onlyNumber = r'^\d+$'
onlyLetters = r'^[a-zA-Z\s]+$'
onlyAge = r'^\d+$'


def insertStudent(student_id, full_name, age):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, full_name) and re.match(onlyAge, age):
        try:
            with sqlite3.connect('C:\\Users\\49162\\PycharmProjects\\schoolManagement\\school\\school.sqlite') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Students (StudentID, Name, Age) VALUES (?, ?, ?)",
                               (student_id, full_name, age))
                conn.commit()
                messagebox.showinfo("Success", "Student successfully added to the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            messagebox.showerror("Error", "An error occurred while adding the student to the database.")
    else:
        print("Invalid input. Only numbers allowed for ID and Age, and only letters for Full Name.")
        messagebox.showerror("Invalid Input", "Please enter valid data.")


def deleteStudent(student_id, full_name, age):
    if re.match(onlyNumber, student_id) and re.match(onlyLetters, full_name) and re.match(onlyAge, age):
        try:
            with sqlite3.connect('C:\\Users\\49162\\PycharmProjects\\schoolManagement\\school\\school.sqlite') as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Students WHERE StudentID = ? AND Name = ? AND Age = ?",
                               (student_id, full_name, age))
                conn.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Student successfully deleted from the database.")
                else:
                    messagebox.showinfo("Not Found", "No student found with the given ID, Name, and Age.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            messagebox.showerror("Error", "An error occurred while deleting the student from the database.")
    else:
        print("Invalid input. Only numbers allowed for ID and Age, and only letters and spaces for Full Name.")
        messagebox.showerror("Invalid Input", "Please enter valid data for ID, Name, and Age.")
