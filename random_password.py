import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation ""
    for i in range(length):