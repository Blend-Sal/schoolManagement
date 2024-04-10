from tkinter import *
import customtkinter
from backendSchool import create_table

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

buttonStudent = customtkinter.CTkButton(windowMenu, text="Student", command=buttonToStudent)
buttonStudent.pack(anchor=CENTER)

buttonMenu = customtkinter.CTkButton(studentEntry, text="Menu", command=buttonToMenu)
buttonMenu.pack(anchor=CENTER, ipadx=20, ipady=20)

windowMenu.mainloop()
