# Random password generator
import string
import random


def generate_password(length=8, uppercase=True, lowercase=True, digits=True, symbols=False):

    # Generate a random password with specified criteria.
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError('No character types selected.')

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("This program generates strong random passwords!")
password_length = int(input("The password should have how many characters: "))
randompassword = generate_password(length=password_length, uppercase=True, lowercase=True, digits=True, symbols=True)
print(randompassword)
