import ctk_class
import password_input_class
import pw_window_manager_class as pwm
import data_base_manager_class

#creates an sqlite3 database or connects to it if one already exists
database = data_base_manager_class.DatabaseManager()

# development password
PASSWORD = "password"

# creates the main window in a disabled state with access to the database object
window = ctk_class.Window(database)

# creates the password input window
pass_input = password_input_class.PassInput()

# gets the value entered in the text box in the password entry window
pw = pass_input.get_input()

# passes in the arguments required for the PassWindowManager class, i.e., the window in the ctk_class file
# creates the functionality for taking in the pw variable and checking if it is correct
# unlocks the main window is pw == PASSWORD (currently)
# currently allows for unlimited password attempts
password_manager = pwm.PassWindowManager(window, PASSWORD)
password_manager.check_password(pw)



window.mainloop()
