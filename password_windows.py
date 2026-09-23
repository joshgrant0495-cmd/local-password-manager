import customtkinter as ctk
import security_manager as hasher
from pathlib import Path

MAIN_COLOUR = "#0A174E"
SECONDARY_COLOUR = "#F5D042"
HOVER_COLOUR = "#f2e985"


class PasswordManager:
    """
    Checks whether the relevant hashed password and salt files exist,
    creating a login window if they do, or prompting the user to create
    a password if they do not - this saves the relevant files for
    future login attempts so that the login window only shows.
    """
    def __init__(self):
        self.pass_hash = hasher.SecurityManager()

    def create_pass_window(self):
        self.create_window = ctk.CTk()
        self.create_window.geometry("350x250")
        self.create_window.title("Create a Password")
        self.create_window.configure(fg_color=MAIN_COLOUR, padx=10, pady=10)

        self.set_pass = ctk.CTkEntry(master=self.create_window, width=250, height=40, corner_radius=10,
                                     bg_color=MAIN_COLOUR,
                                       placeholder_text="Enter a password",
                                       border_color="black",
                                       font=("Segoe UI", 16),
                                       border_width=2)
        self.set_pass.grid(row=1, column=0, sticky="s", padx=10, pady=10)

        self.confirm_pass = ctk.CTkEntry(master=self.create_window, width=250, height=40, corner_radius=10,
                                     bg_color=MAIN_COLOUR,
                                     placeholder_text="Confirm Your Password",
                                     border_color="black",
                                     font=("Segoe UI", 16),
                                     border_width=2)
        self.confirm_pass.grid(row=2, column=0, sticky="s", padx=10, pady=10)

        self.accept_password = ctk.CTkButton(master=self.create_window,text="Set Password",
                                    width=100, height=40,
                                    fg_color=SECONDARY_COLOUR, hover_color=HOVER_COLOUR,
                                    text_color=MAIN_COLOUR,
                                    border_color="black",
                                    font=("Segoe UI", 16),
                                    command=self.check_pass_match
                                             )
        self.accept_password.grid(row=3, column=0, padx=10, pady=10)
        self.create_window.mainloop()

    def check_pass_match(self):
        pass_one = self.set_pass.get()
        pass_two = self.confirm_pass.get()
        if pass_one == pass_two:
            self.pass_hash.hash_password(pass_one)
            self.password = pass_one
            self.create_window.destroy()
        else:
            self.set_pass.delete(0, "end")
            self.confirm_pass.delete(0, "end")
            self.create_window.title("Passwords Need to Match!")


    def login(self):

        self.login_window = ctk.CTk()
        self.login_window.geometry("400x100")
        self.login_window.title("Password Entry")
        self.login_window.configure(
            fg_color=MAIN_COLOUR,
            padx=10,
            pady=10
        )

        self.pass_input = ctk.CTkEntry(
            master=self.login_window,
            width=250,
            height=40,
            corner_radius=10,
            bg_color=MAIN_COLOUR,
            placeholder_text="Enter your password",
            border_color="black",
            font=("Segoe UI", 16),
            border_width=2,
            show="*"
        )
        self.pass_input.grid(row=1, column=1, padx=10, pady=10)


        self.login_button = ctk.CTkButton(
            master=self.login_window,
            text="Login",
            width=100,
            height=40,
            fg_color=SECONDARY_COLOUR,
            hover_color=HOVER_COLOUR,
            text_color=MAIN_COLOUR,
            border_color="black",
            font=("Segoe UI", 16),
            command=self.check_login
        )
        self.login_button.grid(row=1, column=2, padx=10, pady=10)

        self.login_window.mainloop()

    def check_login(self):
        password = self.pass_input.get()

        if self.pass_hash.check_password(password):
            self.password = password
            self.login_window.destroy()
        else:
            self.pass_input.delete(0, "end")
            self.login_window.title("Incorrect Password")

    def start_authentication(self):
        if Path("master_password/hashed_password.txt").exists() and Path(
                "master_password/password_salt.txt").exists():
            self.login()
        else:
            self.create_pass_window()
