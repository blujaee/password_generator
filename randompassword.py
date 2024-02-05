import random
import string

def random_password_generator():

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    password_array = []
    password_index = 0

    number_of_passwords = int(input("Enter the number of passwords you would like to generate: "))
    password_length = int(input("Enter the desired length for the password: "))
    include_uppercase = input("Do you want uppercase letters in your password? ")
    if (include_uppercase.lower() == "yes"):
        include_uppercase = True
    else: include_uppercase = False
    include_digits = input("Do you want numbers in your password? ")
    if (include_digits.lower() == "yes"):
        include_digits = True
    else:
        include_digits = False
    include_special_chars = input("Do you want special characters in your password? ")
    if (include_special_chars.lower() == "yes"):
        include_special_chars = True
    else:
        include_special_chars = False
    # creates a pool out of the selected types of characters
    character_pool = lowercase

    if include_uppercase:
        character_pool += uppercase
    if include_digits:
        character_pool += digits
    if include_special_chars:
        character_pool += special_chars

    for _ in range(number_of_passwords):
        password = ''.join(random.choice(character_pool) for _ in range(password_length))
        password_array.append(password)
    
    print("Generated Passwords: ")
    for _ in range(number_of_passwords):
        print(password_array[password_index])
        password_index += 1

random_password_generator()