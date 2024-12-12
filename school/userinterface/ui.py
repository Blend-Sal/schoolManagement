from school.backend.db_operations import *  # Import backend database functions
import customtkinter as ctk
from tkinter import *


# Main window configuration
window = ctk.CTk()  # Create the main application window using CustomTkinter
window.title("Menu")  # Set the title of the window
window.geometry("1920x1080")  # Set the window size to full HD resolution

def show_frame(frame):
    """Bring the specified frame to the front."""
    frame.tkraise()

# Frames for main menu and student menu
main_menu = ctk.CTkFrame(window)  # Main menu frame
student_menu = ctk.CTkFrame(window)  # Student menu frame

# Place the frames to cover the entire window
for frame in (main_menu, student_menu):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Main menu buttons
buttonStudent = ctk.CTkButton(
    main_menu, text="Student", width=300, height=50, font=("Arial", 20),
    command=lambda: show_frame(student_menu)  # Navigate to the student menu
)
buttonStudent.pack(anchor=CENTER, pady=10)

buttonToQuit = ctk.CTkButton(
    main_menu, text="Quit", width=300, height=50, font=("Arial", 20),
    command=window.destroy  # Close the application
)
buttonToQuit.pack(anchor=CENTER, pady=10)

# Student menu labels and entry fields
# Student ID input
labelStudentID = ctk.CTkLabel(student_menu, text="Student ID:", font=("Arial", 20))
labelStudentID.pack(anchor=CENTER, pady=(20, 5))

entryStudentID = ctk.CTkEntry(student_menu, width=300, height=40, font=("Arial", 20))
entryStudentID.pack(anchor=CENTER, pady=10)

# Student Name input
labelStudentName = ctk.CTkLabel(student_menu, text="Student Name:", font=("Arial", 20))
labelStudentName.pack(anchor=CENTER, pady=(20, 5))

entryStudentName = ctk.CTkEntry(student_menu, width=300, height=40, font=("Arial", 20))
entryStudentName.pack(anchor=CENTER, pady=10)

# Student Age input
labelStudentAge = ctk.CTkLabel(student_menu, text="Student Age:", font=("Arial", 20))
labelStudentAge.pack(anchor=CENTER, pady=(20, 5))

entryStudentAge = ctk.CTkEntry(student_menu, width=300, height=40, font=("Arial", 20))
entryStudentAge.pack(anchor=CENTER, pady=10)

# Buttons in the student menu
# Create student button
buttonStudentTable = ctk.CTkButton(
    student_menu, text="Create Student", width=300, height=50, font=("Arial", 20),
    command=lambda: insertStudent(
        entryStudentID.get().strip(),
        entryStudentName.get().strip(),
        entryStudentAge.get().strip()
    )
)
buttonStudentTable.pack(anchor=CENTER, pady=10)

# Delete student button
buttonDeleteStudent = ctk.CTkButton(
    student_menu, text="Delete Student", width=300, height=50, font=("Arial", 20),
    command=lambda: deleteStudent(
        entryStudentID.get().strip(),
        entryStudentName.get().strip(),
        entryStudentAge.get().strip()
    )
)
buttonDeleteStudent.pack(anchor=CENTER, pady=10)

# Update student button
buttonToUpdateStudent = ctk.CTkButton(
    student_menu, text="Update Student", width=300, height=50, font=("Arial", 20),
    command=lambda: updateStudent(
        entryStudentID.get().strip(),
        entryStudentName.get().strip(),
        entryStudentAge.get().strip()
    )
)
buttonToUpdateStudent.pack(anchor=CENTER, pady=10)

# Back to main menu button
buttonMenu = ctk.CTkButton(
    student_menu, text="Back to Menu", width=300, height=50, font=("Arial", 20),
    command=lambda: show_frame(main_menu)  # Navigate back to the main menu
)
buttonMenu.pack(anchor=CENTER, pady=10)

# Quit button in the student menu
buttonToQuitStudent = ctk.CTkButton(
    student_menu, text="Quit", width=300, height=50, font=("Arial", 20),
    command=window.destroy  # Close the application
)
buttonToQuitStudent.pack(anchor=CENTER, pady=10)

# Show the main menu frame on startup
show_frame(main_menu)

# Run the application
window.mainloop()
