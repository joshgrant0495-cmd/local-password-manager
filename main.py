from pathlib import Path
import os
import sys

import ctk_window
import database_manager
import password_windows
import security_manager

if getattr(sys, "frozen", False):
    app_directory = Path(sys.executable).parent
else:
    app_directory = Path(__file__).parent
os.chdir(app_directory)

# creates the password manager and starts the authentication process
# then retains the authenticated password in memory for database encryption/decryption
password_manager = password_windows.PasswordManager()
password_manager.start_authentication()
password = password_manager.password

security_manager.SecurityManager().check_salt_path(password)

# creates an sqlite3 database or connects to it if one already exists
database = database_manager.DatabaseManager()

# creates the main window with access to the database object
window = ctk_window.Window(database)

def close_window():
    """
    Closes the database connection, encrypts the database file,
    then closes the application.
    """
    database.close_database()
    security_manager.SecurityManager().encrypt_file(
        file_path="master_encryption/password.db",
        password=password
    )
    window.destroy()

# registers close_window as the callback for the window close event,
# allowing the database to be closed and encrypted before the application exits
window.protocol("WM_DELETE_WINDOW", close_window)

window.mainloop()
