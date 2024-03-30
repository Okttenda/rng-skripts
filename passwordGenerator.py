import random
import string

def get_user_input():
    user_input = input("How many Characters should your password have? : ")
    characters = int(user_input)
    printables = string.printable
    i = 0
    password = []
    while i < characters:
        letter = random.choice(printables)
        password.append(letter)
        i += 1
    return password


t1 = get_user_input()
password = "".join(t1)
print(password)