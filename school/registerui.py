from tkinter import *
import customtkinter as ctk
from school.db_operations import *


registerWindow = ctk.CTk()
registerWindow.geometry("1920x1080")
registerWindow.title("Register")


registerEntryName = ctk.CTkEntry(placeholder_text="Name", command=insertRegisterStudent())
registerEntryName.place(relx=.5, rely=.5)
