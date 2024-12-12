from school.backend.db_operations import *
from tkinter import messagebox
import re

onlyNumber = r'^\d+$'
onlyLetters = r'^[a-zA-Z\s]+$'
onlyAge = r'^\d+$'
onlyPassword = r'^[a-zA-Z0-9\s]+$'


#def if_teacher_exists(full_name, age, password):


def validate_input_Teacher(student_id, full_name=None, age=None):
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

def valitade_input_Register(full_name=None, age=None, password="<PASSWORD>"):
    if not re.match(onlyLetters, full_name):
        messagebox.showerror("Invalid Input", "Full name must contain only letters and spaces.")
        return False
    if not re.match(onlyAge, age):
        messagebox.showerror("Invalid Input", "Age must be numeric.")
        return False
    if not re.match(password, onlyPassword):
        messagebox.showerror("Invalid Input", "Password must be numeric and contain letters.")
        return False
    return True
