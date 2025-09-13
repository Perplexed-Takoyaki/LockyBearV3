
from cryptography.fernet import Fernet


def encrypt(data, master_key):
    f = Fernet(master_key)
    encrypted = f.encrypt(data.encode())
    print("encrypted : ", encrypted)
    return encrypted



def decrypt(encrypted_data, master_key):
    f = Fernet(master_key)
    decrypted = f.decrypt(encrypted_data).decode()
    print("decrypted : ", decrypted)
    return decrypted
