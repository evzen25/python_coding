import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&()")

def generate_password():
    password_length = int(input("How long would you like your password to  be? "))

    random.shuffle(characters)

    passwword = []

    for x in range(password_length):
        passwword.append(random.choice(characters))

    random.shuffle(passwword)

    passwword = "".join(passwword)

    print(passwword)

option = input ("Do you want to generate a password? (Yes/No) ")

while option != "end":
    if option == "Yes":
        generate_password()
    elif option == "No":
        print("Program ended")
        quit()
    else:
        print("Invalid input, please input Yes, No, or end")

    option = input("Do you want to generate a password? (Yes/No) ")