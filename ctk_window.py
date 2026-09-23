import customtkinter as ctk
import password_generator as p_gen
from user_info_window import InformationPopupWindow

MAIN_COLOUR = "#0A174E"
SECONDARY_COLOUR = "#F5D042"
HOVER_COLOUR = "#f2e985"

class Window(ctk.CTk):
    """Creates the main window's username, password, password generator text box,
    and info retrieval dropdown, along with associated buttons."""
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.geometry("500x350")
        self.title("My Local Password Manager")
        self.configure(fg_color=MAIN_COLOUR, padx=10, pady=10)


        # creates entry boxes to fit on the grid system above
        self.name_entry = ctk.CTkEntry(master=self, width=250, height=40, corner_radius=10,
                                     bg_color=MAIN_COLOUR,
                                       placeholder_text="Enter a name, i.e., Facebook",
                                       border_color="black",
                                       font=("Segoe UI", 16),
                                       border_width=2,
                                    )
        self.name_entry.grid(row=1, column=0, sticky="w", padx=10, pady=(10, 10))

        self.un_entry = ctk.CTkEntry(master=self, width=250, height=40, corner_radius=10,
                                     placeholder_text="Enter your username",
                                     bg_color=MAIN_COLOUR,
                                     border_color="black",
                                     font=("Segoe UI", 16),
                                     )
        self.un_entry.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.pw_entry = ctk.CTkEntry(master=self, width=250, height=40, corner_radius=10,
                                     placeholder_text="Enter your password",
                                     bg_color=MAIN_COLOUR,
                                     border_color="black",
                                     font=("Segoe UI", 16),
                                     )
        self.pw_entry.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.info_entry = ctk.CTkEntry(master=self, width=250, height=40, corner_radius=10,
                                     placeholder_text="Enter additional information?",
                                     bg_color=MAIN_COLOUR,
                                     border_color="black",
                                     font=("Segoe UI", 16),
                                     )
        self.info_entry.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.gen_entry = ctk.CTkEntry(master=self, width=250, height=40, corner_radius=10,
                                     placeholder_text="Click generate password",
                                     bg_color=MAIN_COLOUR,
                                     border_color="black",
                                     font=("Segoe UI", 16),)

        self.gen_entry.grid(row=5, column=0, sticky="w", padx=10, pady=(20,10))

        # creates generate and save buttons
        self.pw_gen = ctk.CTkButton(master=self, text="Generate Password", width=200, height=40,
                                    fg_color=SECONDARY_COLOUR, hover_color=HOVER_COLOUR,
                                    text_color=MAIN_COLOUR,
                                    border_color="black",
                                    font=("Segoe UI", 16),
                                    command=self.add_strong_password
                                    )
        self.pw_gen.grid(row=5, column=1, sticky="w", padx=(0, 5), pady=(20,10))

        self.save_button = ctk.CTkButton(master=self, text="Save", width=100, height=40,
                                         fg_color=SECONDARY_COLOUR,
                                         text_color=MAIN_COLOUR,
                                         hover_color=HOVER_COLOUR,
                                         border_color="black",
                                         font=("Segoe UI", 16),
                                         command=self.add_user_info)
        self.save_button.grid(row=4, column=1, sticky="w", padx=(0, 5), pady=10)

        # creates a combobox to display database names,
        # then retrieves username, password, and information values for
        # a selected name and displays them in a popup window
        self.add_info = ctk.CTkComboBox(master=self, width=250, height=40,
                                        button_color=SECONDARY_COLOUR,
                                        hover=True,
                                        dropdown_text_color="black",
                                        border_color="black",
                                        dropdown_font=("Segoe UI", 16),
                                        font=("Segoe UI", 16),
                                        command=self.populate_popup
                                        )
        self.add_info.set(value="Select name to retrieve info")
        self.add_info.grid(row=6, column=0, sticky="w", padx=10)
        self.populate_names()


    def add_strong_password(self):
        """takes the create password method and configures
        the associated gen_entry textbox to display it"""
        strong_password = p_gen.GeneratePassword().create_password()
        self.gen_entry.delete(0, "end")
        self.gen_entry.insert(0, strong_password)


    def add_user_info(self):
        name_entry = self.name_entry.get()
        user_name_entry = self.un_entry.get()
        pass_entry = self.pw_entry.get()
        info_entry = self.info_entry.get()

        self.database.save_record(name_entry, user_name_entry, pass_entry, info_entry)

        self.name_entry.delete(0, "end")
        self.gen_entry.delete(0, "end")
        self.un_entry.delete(0, "end")
        self.pw_entry.delete(0, "end")
        self.info_entry.delete(0, "end")

        self.populate_names()


    def populate_names(self):
        new_names = self.database.retrieve_names()
        self.add_info.configure(values=new_names)
        self.add_info.set("Select name to retrieve info")


    def populate_popup(self, selected_name):
        record = self.database.get_db_info(selected_name)
        if record is not None:
            InformationPopupWindow(self, record)
