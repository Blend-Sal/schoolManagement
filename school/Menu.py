from tkinter import *
import customtkinter as ctk
from school.backendSchool import insertStudent, deleteStudent

windowMenu = ctk.CTk()
studentEntry = ctk.CTkToplevel()
windowMenu.title("Menu")
windowMenu.geometry("1280x720")


def buttonToMenu():
    studentEntry.withdraw()
    windowMenu.deiconify()


def buttonToStudent():
    windowMenu.withdraw()
    studentEntry.title("Student Entry")
    studentEntry.geometry("1280x720")
    studentEntry.deiconify()


entryStudentID = (ctk.CTkEntry(studentEntry))
entryStudentID.pack(anchor=CENTER)

entryStudentName = ctk.CTkEntry(studentEntry)
entryStudentName.pack(anchor=CENTER)

entryStudentAge = ctk.CTkEntry(studentEntry)
entryStudentAge.pack(anchor=CENTER)

buttonStudentTable = ctk.CTkButton(studentEntry, text="Create Student",
                                   command=lambda: insertStudent(entryStudentID.get().strip(),
                                                                 entryStudentName.get().strip(),
                                                                 entryStudentAge.get().strip()))
buttonStudentTable.pack(anchor=CENTER)

buttonStudent = ctk.CTkButton(windowMenu, text="Student", command=buttonToStudent)
buttonStudent.pack(anchor=CENTER)

buttonMenu = ctk.CTkButton(studentEntry, text="Menu", command=buttonToMenu)
buttonMenu.pack(anchor=CENTER)

buttonDeleteStudent = ctk.CTkButton(studentEntry, text="Delete Student",
                                    command=lambda: deleteStudent(entryStudentID.get().strip(),
                                                                  entryStudentName.get().strip(),
                                                                  entryStudentAge.get().strip()))
buttonDeleteStudent.pack(anchor=CENTER)

buttonToQuit = ctk.CTkButton(windowMenu, text="Quit", command=windowMenu.destroy)
buttonToQuit.pack(anchor=CENTER)

buttonToQuitStudent = ctk.CTkButton(studentEntry, text="Quit", command=studentEntry.destroy)
buttonToQuitStudent.pack(anchor=CENTER)

windowMenu.mainloop()
