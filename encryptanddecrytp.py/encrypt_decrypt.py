import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def get_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

salt = b"my_fixed_salt_1234"  # keep this the same for encrypt and decrypt
password = input("Enter secret key/password: ")

key = get_key_from_password(password, salt)
fernet = Fernet(key)

choice = input("1 for encrypt, 2 for decrypt: ")

if choice == "1":
    message = input("Enter message to encrypt: ")
    encrypted = fernet.encrypt(message.encode())
    print("Encrypted:", encrypted.decode())

elif choice == "2":
    token = input("Enter encrypted text: ")
    decrypted = fernet.decrypt(token.encode())
    print("Decrypted:", decrypted.decode())