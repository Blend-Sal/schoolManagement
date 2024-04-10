from tkinter import *
import customtkinter
from backendSchool import insertStudent

windowMenu = customtkinter.CTk()
studentEntry = customtkinter.CTk()
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


entryStudentID = customtkinter.CTkEntry(studentEntry)
entryStudentID.pack(anchor=CENTER)

entryStudentName = customtkinter.CTkEntry(studentEntry)
entryStudentName.pack(anchor=CENTER)

entryStudentAge = customtkinter.CTkEntry(studentEntry)
entryStudentAge.pack(anchor=CENTER)

buttonStudentTable = customtkinter.CTkButton(studentEntry, text="Create Student",
                                             command=insertStudent(entryStudentID.get(), entryStudentName.get(),
                                                                   entryStudentAge.get()))

buttonStudentTable.pack(anchor=CENTER)

buttonStudent = customtkinter.CTkButton(windowMenu, text="Student", command=buttonToStudent)
buttonStudent.pack(anchor=CENTER)

buttonMenu = customtkinter.CTkButton(studentEntry, text="Menu", command=buttonToMenu)
buttonMenu.pack(anchor=CENTER)

windowMenu.mainloop()
