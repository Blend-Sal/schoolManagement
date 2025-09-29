from school.backend.db_validation import *
from school.backend.db_securefeatures import *

insertStudentQuery = "INSERT INTO Students (StudentID, Name, Age) VALUES (%s, %s, %s)"
deleteStudentQuery = "DELETE FROM Students WHERE StudentID = %s AND Name = %s AND Age = %s"
updateStudentQuery = "UPDATE Students SET Name = %s,    Age = %s WHERE StudentID = %s"
insertRegisterQuery = "INSERT INTO Students (Name, Age, password) VALUES (%s, %s, %s)"

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def insertRegisterStudent(full_name, age, password):
    if valitade_input_Register(full_name, age, password):
        create_table_if_not_exists_teacher()
        rowcount = execute_query(insertRegisterStudent, (full_name, age, password))
        if rowcount:
            messagebox.showinfo("Successfully Registered", "You successfully registered")
        else:
            messagebox.showerror("Not successfully Registered", "Student not Registered")


def insertStudent(student_id, full_name, age):
    """Insert a new student into the database."""
    if validate_input_Teacher(student_id, full_name, age):
        create_table_if_not_exists_student()
        rowcount = execute_query(insertStudentQuery, (int(student_id), full_name, int(age)))
        if rowcount:
            messagebox.showinfo("Success", "Student successfully added to the database.")
        else:
            messagebox.showerror("Error", "An error occurred while adding the student.")


def deleteStudent(student_id, full_name, age):
    """Delete a student from the database."""
    if validate_input_Teacher(student_id, full_name, age):
        rowcount = execute_query(deleteStudentQuery, (int(student_id), full_name, int(age)))
        if rowcount > 0:
            messagebox.showinfo("Success", "Student successfully deleted from the database.")
        else:
            messagebox.showinfo("Not Found", "No student found with the given ID, Name, and Age.")


def updateStudent(student_id, new_name, new_age):
    """Update a student's name and age in the database."""
    if validate_input_Teacher(student_id, full_name=new_name, age=new_age):
        create_table_if_not_exists_student()
        rowcount = execute_query(
            updateStudentQuery,
            (new_name, new_age, int(student_id))
        )
        if rowcount > 0:
            messagebox.showinfo("Success", "Student successfully updated in the database.")
        else:
            messagebox.showinfo("Not Found", "No student found with the given ID.")
