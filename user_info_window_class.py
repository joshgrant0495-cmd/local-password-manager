import customtkinter as ctk
import pyperclip as pyp

MAIN_COLOUR = "#0A174E"
SECONDARY_COLOUR = "#F5D042"
HOVER_COLOUR = "#f2e985"

"""this is a test file to configure the pop up window once the name has been
selected from the add_info combobox. 
I have created a retrieve_data method in the Window class in the ctk_class file.
The retrieve_data method takes in the SQL retrieved from get_db_info method in 
the DatabaseManager class"""

class InformationPopupWindow(ctk.CTkToplevel):
    def __init__(self, parent, record):
        super().__init__(parent)

        self.geometry("410x400")
        self.title("Password Manager")
        self.label = ctk.CTkLabel(self, text="")
        self.configure(fg_color=MAIN_COLOUR)

        self.user_name_retrieval = ctk.CTkTextbox(master=self, state="normal", width=300, height=20,
                                             border_color=SECONDARY_COLOUR,
                                             font=("Segoe UI", 16), border_width=2,
                                             )
        self.user_name_retrieval.insert(index=0.0, text="Username: ")
        self.user_name_retrieval.grid(row=0, column=0, padx=20, pady=20)

        self.password_retrieval = ctk.CTkTextbox(master=self, state="normal", width=300, height=20,
                                             border_color=SECONDARY_COLOUR,
                                             font=("Segoe UI", 16), border_width=2,
                                             )
        self.password_retrieval.insert(index=0.0, text="Password: ")
        self.password_retrieval.grid(row=1, column=0, padx=20, pady=20)

        self.info_retrieval = ctk.CTkTextbox(master=self, state="normal", width=300, height=150,
                                             border_color=SECONDARY_COLOUR,
                                             font=("Segoe UI", 16), border_width=2,
                                             activate_scrollbars=True, scrollbar_button_color=SECONDARY_COLOUR,
                                             scrollbar_button_hover_color=HOVER_COLOUR)
        self.info_retrieval.insert(index=0.0, text="Your information: ")
        self.info_retrieval.grid(row=2, column=0, padx=20, pady=20)

        self.unr_copy = ctk.CTkButton(master=self, width=35, height=35, fg_color=SECONDARY_COLOUR,
                                     hover_color=HOVER_COLOUR, text="Copy", text_color="black",
                                     font=("Segoe UI", 18),
                                      command=self.copy_un)
        self.unr_copy.grid(row=0, column=1)

        self.pr_copy = ctk.CTkButton(master=self, width=35, height=35, fg_color=SECONDARY_COLOUR,
                                     hover_color=HOVER_COLOUR, text="Copy", text_color="black",
                                     font=("Segoe UI", 18),
                                     command=self.copy_pw)
        self.pr_copy.grid(row=1, column=1)

        self.populate(record)

    def populate(self, record):
        self.user_name_retrieval.insert("end", record["username"])
        self.password_retrieval.insert("end", record["password"])
        self.info_retrieval.insert("end", record["information"])

        self.username = record["username"]
        self.password = record["password"]

    def copy_un(self):
        pyp.copy(self.username)

    def copy_pw(self):
        pyp.copy(self.password)

