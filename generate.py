import sys
import string
import random

def get_password_length():
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number as an argument")
        sys.exit(1)
    return length

def get_excluded_characters():
    try:
        excluded_characters = sys.argv[2:]
    except IndexError:
        return ""
    return excluded_characters

length = int(get_password_length())
excluded_characters = get_excluded_characters()
print(excluded_characters)

password_generating = True
while password_generating == True:
    password = []
    for i in range(length):
        password.append(string.printable[random.randint(0, 93)]) 
        if any(char in excluded_characters for char in password): #better implemented by removing excluded characters from the printable string
            password_generating = True
        else:
            password_generating = False


print("".join(password))


