import sys
import string
import random

def get_arguments():
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number as an argument")
        sys.exit(1)
    return length

length = int(get_arguments())
password = []
for i in range(length):
    password.append(string.printable[random.randint(0, 93)])

print("".join(password))


