from tkinter import *
import customtkinter as ctk
from school.backendSchool import *

windowMenu = ctk.CTk()
studentEntry = ctk.CTkToplevel()
windowMenu.title("Menu")
windowMenu.geometry("1920x1080")


def buttonToMenu():
    studentEntry.withdraw()
    windowMenu.deiconify()


def buttonToStudent():
    windowMenu.withdraw()
    studentEntry.title("Student Entry")
    studentEntry.geometry("1920x1080")
    studentEntry.deiconify()


entryStudentID = ctk.CTkEntry(studentEntry, width=300, height=40, font=("Arial", 20))
entryStudentID.pack(anchor=CENTER, pady=10)

entryStudentName = ctk.CTkEntry(studentEntry, width=300, height=40, font=("Arial", 20))
entryStudentName.pack(anchor=CENTER, pady=10)

entryStudentAge = ctk.CTkEntry(studentEntry, width=300, height=40, font=("Arial", 20))
entryStudentAge.pack(anchor=CENTER, pady=10)

buttonStudentTable = ctk.CTkButton(studentEntry, text="Create Student", width=300, height=50, font=("Arial", 20),
                                   command=lambda: insertStudent(entryStudentID.get().strip(),
                                                                 entryStudentName.get().strip(),
                                                                 entryStudentAge.get().strip()))
buttonStudentTable.pack(anchor=CENTER, pady=10)

buttonStudent = ctk.CTkButton(windowMenu, text="Student", width=300, height=50, font=("Arial", 20),
                              command=buttonToStudent)
buttonStudent.pack(anchor=CENTER, pady=10)

buttonMenu = ctk.CTkButton(studentEntry, text="Menu", width=300, height=50, font=("Arial", 20), command=buttonToMenu)
buttonMenu.pack(anchor=CENTER, pady=10)

buttonDeleteStudent = ctk.CTkButton(studentEntry, text="Delete Student", width=300, height=50, font=("Arial", 20),
                                    command=lambda: deleteStudent(entryStudentID.get().strip(),
                                                                  entryStudentName.get().strip(),
                                                                  entryStudentAge.get().strip()))
buttonDeleteStudent.pack(anchor=CENTER, pady=10)

buttontoUpdateStudent = ctk.CTkButton(studentEntry, text="Update Student", width=300, height=50, font=("Arial", 20),
                                      command=lambda: updateStudent(entryStudentID.get().strip()))
buttontoUpdateStudent.pack(anchor=CENTER, pady=10)

buttonToQuit = ctk.CTkButton(windowMenu, text="Quit", width=300, height=50, font=("Arial", 20),
                             command=windowMenu.destroy)
buttonToQuit.pack(anchor=CENTER, pady=10)

buttonToQuitStudent = ctk.CTkButton(studentEntry, text="Quit", width=300, height=50, font=("Arial", 20),
                                    command=studentEntry.destroy)
buttonToQuitStudent.pack(anchor=CENTER, pady=10)

windowMenu.mainloop()
