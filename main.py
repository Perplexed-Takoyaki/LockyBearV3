from utils import save_password, retrieve_password
from cryptography.fernet import Fernet
from encryptor import encrypt, decrypt
from random_password import generate_password

print("Welcome to LockyBear! I am going to help you manage passwords! 🐻")

message_1 = input("type 1 for saving password, 2 for retrieving password : ")

if message_1 == "1":
    entity_name = input("What account do you want to save the password of? ")
    #password = input("What is your password for this account? ")
    message_3 = int(input("how many characters do you want in your new password?" ))
    new_password = generate_password(message_3)
    print("your new password is : " + new_password)
    save_password(entity_name, new_password)
    print(f"Password for '{entity_name}' saved successfully!")
    #message_2 = input("do you want to generate a new password? (y/n)")
    #if message_2 == "y":

    #else :
            #print("thank you for using LockyBear!")

elif message_1 == "2":
    entity_name = input("What account do you want to retrieve the password of? ")
    decrypted_password = retrieve_password(entity_name)
    if decrypted_password:
        print(f"The password for '{entity_name}' is: {decrypted_password}")
    else:
        print("Password not found")