import string
import random


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    while len(password) < length:
        password = password + random.choice(characters)
    return password