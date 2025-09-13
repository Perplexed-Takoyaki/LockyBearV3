import os
from cryptography.fernet import Fernet
from encryptor import encrypt, decrypt

#master_key = Fernet.generate_key()
f = open("master_key", "rb")
master_key = f.read()

def save_password(entity_name, password):
    file = entity_name + ".passwd"
    encrypted_password = encrypt(password, master_key)
    f = open(file, "wb")
    f.write(encrypted_password)
    print("Password saved successfully")
    print(file)
    f.close()

def retrieve_password(entity_name):
    file = entity_name + ".passwd"
    if os.path.exists(file):
        f = open(file, "rb")
        encrypted_data = f.read()
        decrypted_password = decrypt(encrypted_data, master_key)
        print("Password retrieved successfully")
        f.close()
        return decrypted_password
    else:
        return "error"