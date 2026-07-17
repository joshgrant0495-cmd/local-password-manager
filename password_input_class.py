import customtkinter as ctk

MAIN_COLOUR = "#0A174E"
SECONDARY_COLOUR = "#F5D042"
HOVER_COLOUR = "#f2e985"


class PassInput(ctk.CTk):
    """opens a dialogue window with a text input for a user to enter a password"""
    def __init__(self):
        super().__init__()

        self.pass_input = ctk.CTkInputDialog(title="Password Entry", text="",
                                             fg_color=MAIN_COLOUR, button_fg_color=SECONDARY_COLOUR,
                                             button_hover_color=HOVER_COLOUR, button_text_color="black",
                                             entry_text_color="black")

    def get_input(self):
        return self.pass_input.get_input()




