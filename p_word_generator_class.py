import random as rnd

LOWERCASE = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

UPPERCASE = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

DIGITS = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

SYMBOLS = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+", "[", "]",
    "{", "}", ";", ":", "'", '"', ",", ".",
    "<", ">", "/", "?", "\\", "|", "`", "~"
]


class GeneratePassword:
    """creates a random password with uppercase, lowercase, digits and special symbols"""
    def create_password(self):
        password = []
        for _ in range(0, 4):
            password.append(rnd.choice(LOWERCASE))
            password.append(rnd.choice(UPPERCASE))
            password.append(rnd.choice(DIGITS))
            password.append(rnd.choice(SYMBOLS))
        rnd.shuffle(password)
        joined_password = "".join(password)
        return joined_password







