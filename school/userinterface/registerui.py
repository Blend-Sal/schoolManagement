from school.backend.db_helper import handle_insert_register
from school.backend.db_operations import *
import customtkinter as ctk
from tkinter import *
from school.userinterface.ui import *


registerWindow = ctk.CTk()
registerWindow.geometry("1920x1080")
registerWindow.title("Register")

registerEntryName = ctk.CTkEntry(placeholder_text="Name", width=300, height=40, font=("Arial", 20))
registerEntryName.pack(anchor=CENTER, pady=10)

registerEntryAge = ctk.CTkEntry(placeholder_text="Age", width=300, height=40, font=("Arial", 20))
registerEntryAge.pack(anchor=CENTER, pady=10)

registerEntryPassword = ctk.CTkEntry(placeholder_text="Password", width=300, height=40, font=("Arial", 20))
registerEntryPassword.pack(anchor=CENTER, pady=10)

insertRegisterButton = ctk.CTkButton(text="Register", command=lambda:handle_insert_register())
insertRegisterButton.pack(anchor=CENTER, pady=10)

registerToTeacher = ctk.CTkButton(text="Login", )

show_frame(registerWindow)

registerWindow.mainloop()
