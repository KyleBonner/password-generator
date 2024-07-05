import sys
import string
import random

def get_arguments():
    length = sys.argv[1]
    return length

length = int(get_arguments())
password = []
for i in range(length):
    password.append(string.printable[random.randint(0, 93)])

print("".join(password))


