from utils import save_password, retrieve_password
from cryptography.fernet import Fernet
from encryptor import encrypt, decrypt

print("Welcome to LockyBear! I am going to help you manage passwords! 🐻")

message_1 = input("type 1 for saving password, 2 for retrieving password")

if message_1 == "1":
    entity_name = input("What account do you want to save the password of? ")
    password = input("What is your password for this account? ")
    save_password(entity_name, password)
    print(f"Password for '{entity_name}' saved successfully!")

elif message_1 == "2":
    entity_name = input("What account do you want to retrieve the password of? ")
    decrypted_password = retrieve_password(entity_name)
    if decrypted_password:
        print(f"The password for '{entity_name}' is: {decrypted_password}")
    else:
        print("Password not found")