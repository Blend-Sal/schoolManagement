from tkinter import *
import customtkinter as ctk
from school.backendSchool import insertStudent

windowMenu = ctk.CTk()
studentEntry = ctk.CTk()
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


entryStudentID = ctk.CTkEntry(studentEntry)
entryStudentID.pack(anchor=CENTER)

entryStudentName = ctk.CTkEntry(studentEntry)
entryStudentName.pack(anchor=CENTER)

entryStudentAge = ctk.CTkEntry(studentEntry)
entryStudentAge.pack(anchor=CENTER)

buttonStudentTable = ctk.CTkButton(studentEntry, text="Create Student",
                                   command=lambda: insertStudent(entryStudentID.get(), entryStudentName.get(),
                                                                 entryStudentAge.get()))
buttonStudentTable.pack(anchor=CENTER)

buttonStudent = ctk.CTkButton(windowMenu, text="Student", command=buttonToStudent)
buttonStudent.pack(anchor=CENTER)

buttonMenu = ctk.CTkButton(studentEntry, text="Menu", command=buttonToMenu)
buttonMenu.pack(anchor=CENTER)

buttonToQuit = ctk.CTkButton(windowMenu, text="Quit", command=windowMenu.destroy)

windowMenu.mainloop()
