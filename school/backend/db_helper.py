from school.userinterface.registerui import *


def handle_insert_register():
    insertRegisterStudent(registerEntryName.get().strip(), registerEntryAge.get().strip(),
                          registerEntryPassword.get().strip())
