import customtkinter as ctk

MAIN_COLOUR = "#0A174E"
SECONDARY_COLOUR = "#F5D042"
HOVER_COLOUR = "#f2e985"

class PassWindowManager:
    """Takes in the window class and password as arguments and checks whether the entered password in the
    PassInput class is correct. If correct the main window in the Window class is unlocked"""
    def __init__(self, window, password):
        self.window = window
        self.password = password

    def check_password(self, pw):
        if pw == self.password:
            self.unlock_widgets()
        else:
            retry_window = ctk.CTkInputDialog(
                title="Incorrect Password",
                text="Enter password again:",
                fg_color=MAIN_COLOUR,
                button_fg_color=SECONDARY_COLOUR,
                button_hover_color=HOVER_COLOUR,
                button_text_color="black",
                entry_text_color="black")

            self.check_password(retry_window.get_input())

    def unlock_widgets(self):
        self.window.name_entry.configure(state="normal")
        self.window.un_entry.configure(state="normal")
        self.window.pw_entry.configure(state="normal")
        self.window.info_entry.configure(state="normal")
        self.window.gen_entry.configure(state="normal")
        self.window.pw_gen.configure(state="normal")
        self.window.save_button.configure(state="normal")
        self.window.add_info.configure(state="normal")


