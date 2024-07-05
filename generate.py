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
password = []

for i in range(length):
    password.append(string.printable[random.randint(0, 93)])

print("".join(password))


