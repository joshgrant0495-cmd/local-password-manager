from secrets import choice
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+"

class GeneratePassword:
    """
    creates a random password with uppercase, lowercase, digits and a defined list of symbols.
    """
    def create_password(self):
        password = (choice(LOWER + UPPER + DIGITS + SYMBOLS)
        for _ in range(16))
        password = "".join(password)
        return password
