import hashlib
from hashlib import scrypt
import secrets
import cryptography.fernet as fernet
import base64
from pathlib import Path

class SecurityManager:
    def hash_password(self, password: str):
        password_directory = Path("master_password")
        password_directory.mkdir(exist_ok=True)

        salt = secrets.token_bytes(16)
        with open("master_password/password_salt.txt", "wb") as file:
            file.write(salt)

        hashed_password = scrypt(password.encode(),
                                         salt=salt,
                                         n=16384,
                                         r=8,
                                         p=5)

        with open("master_password/hashed_password.txt", "wb") as file:
            file.write(hashed_password)

    def check_password(self, password: str):
        with open("master_password/password_salt.txt", "rb") as salted_file:
            salt = salted_file.read()
        with open("master_password/hashed_password.txt", "rb") as hashed_file:
            stored_hash = hashed_file.read()

        hashed_password = scrypt(password.encode(),
                                         salt=salt,
                                         n=16384,
                                         r=8,
                                         p=5)

        return secrets.compare_digest(stored_hash, hashed_password)

    def encrypt_file(self, file_path, password):
        file_path = Path(file_path)
        file_data = file_path.read_bytes()

        password = password.encode()

        salt_path = Path("master_encryption/file_salt.txt")
        if not salt_path.exists():
            salt = secrets.token_bytes(16)
            salt_path.write_bytes(salt)
        else:
            salt = salt_path.read_bytes()

        derived_key = hashlib.scrypt(password,
                                     salt=salt,
                                     n=16384,
                                     r=8,
                                     p=5,
                                     dklen=32)

        fernet_key = base64.urlsafe_b64encode(derived_key)
        fernet_cipher = fernet.Fernet(fernet_key)

        encrypted_file = fernet_cipher.encrypt(file_data)

        file_path.write_bytes(encrypted_file)

    def decrypt_file(self, file_path, password):
        encrypted_file = Path(file_path).read_bytes()

        password = password.encode()

        salt = Path("master_encryption/file_salt.txt").read_bytes()

        derived_key = hashlib.scrypt(password,
                                     salt=salt,
                                     n=16384,
                                     r=8,
                                     p=5,
                                     dklen=32)

        fernet_key = base64.urlsafe_b64encode(derived_key)
        fernet_cipher = fernet.Fernet(fernet_key)

        data_base = fernet_cipher.decrypt(encrypted_file)
        Path(file_path).write_bytes(data_base)

    def check_salt_path(self, password):
        salt_path = Path("master_encryption/file_salt.txt")
        if salt_path.exists():
            self.decrypt_file(file_path="master_encryption/password.db", password=password)




