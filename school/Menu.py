from tkinter import *
import customtkinter as ctk
from school.backendSchool import *

# Main window
window = ctk.CTk()
window.title("Menu")
window.geometry("1920x1080")

def show_frame(frame):
    frame.tkraise()

main_menu = ctk.CTkFrame(window)
student_menu = ctk.CTkFrame(window)

for frame in (main_menu, student_menu):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

buttonStudent = ctk.CTkButton(main_menu, text="Student", width=300, height=50, font=("Arial", 20),
                              command=lambda: show_frame(student_menu))
buttonStudent.pack(anchor=CENTER, pady=10)

buttonToQuit = ctk.CTkButton(main_menu, text="Quit", width=300, height=50, font=("Arial", 20),
                             command=window.destroy)
buttonToQuit.pack(anchor=CENTER, pady=10)

labelStudentID = ctk.CTkLabel(student_menu, text="Student ID:", font=("Arial", 20))
labelStudentID.pack(anchor=CENTER, pady=(20, 5))

entryStudentID = ctk.CTkEntry(student_menu, width=300, height=40, font=("Arial", 20))
entryStudentID.pack(anchor=CENTER, pady=10)

labelStudentName = ctk.CTkLabel(student_menu, text="Student Name:", font=("Arial", 20))
labelStudentName.pack(anchor=CENTER, pady=(20, 5))

entryStudentName = ctk.CTkEntry(student_menu, width=300, height=40, font=("Arial", 20))
entryStudentName.pack(anchor=CENTER, pady=10)

labelStudentAge = ctk.CTkLabel(student_menu, text="Student Age:", font=("Arial", 20))
labelStudentAge.pack(anchor=CENTER, pady=(20, 5))

entryStudentAge = ctk.CTkEntry(student_menu, width=300, height=40, font=("Arial", 20))
entryStudentAge.pack(anchor=CENTER, pady=10)

buttonStudentTable = ctk.CTkButton(student_menu, text="Create Student", width=300, height=50, font=("Arial", 20),
                                   command=lambda: insertStudent(entryStudentID.get().strip(),
                                                                 entryStudentName.get().strip(),
                                                                 entryStudentAge.get().strip()))
buttonStudentTable.pack(anchor=CENTER, pady=10)

buttonMenu = ctk.CTkButton(student_menu, text="Back to Menu", width=300, height=50, font=("Arial", 20),
                           command=lambda: show_frame(main_menu))
buttonMenu.pack(anchor=CENTER, pady=10)

buttonDeleteStudent = ctk.CTkButton(student_menu, text="Delete Student", width=300, height=50, font=("Arial", 20),
                                    command=lambda: deleteStudent(entryStudentID.get().strip(),
                                                                  entryStudentName.get().strip(),
                                                                  entryStudentAge.get().strip()))
buttonDeleteStudent.pack(anchor=CENTER, pady=10)

buttonToUpdateStudent = ctk.CTkButton(student_menu, text="Update Student", width=300, height=50, font=("Arial", 20),
                                      command=lambda: updateStudent(entryStudentID.get().strip()))
buttonToUpdateStudent.pack(anchor=CENTER, pady=10)

buttonToQuitStudent = ctk.CTkButton(student_menu, text="Quit", width=300, height=50, font=("Arial", 20),
                                    command=window.destroy)
buttonToQuitStudent.pack(anchor=CENTER, pady=10)

show_frame(main_menu)

window.mainloop()
