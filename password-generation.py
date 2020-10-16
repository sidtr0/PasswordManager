import random

def Password(length, caps, numbers, symbols):
    
    alphabet_highercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "1234567890"
    symbol = "`~!@#$%^&*()-_=+[{]}\\|:;\"\'<,>.?/"
    string = "abcdefghijklmnopqrstuvwxyz"
    password = ""


    if caps:
        string += alphabet_highercase
    
    if numbers:
        string += number

    if symbols:
        string += symbol

    string = list(string)

    for i in range(length):
        password += random.choice(string)

    return password

    

def main():
    print("Welcome to password generator \n YOur very own personal password generator \n Note: NO password is stored locally. They are generated and then forgotten")

    length_check = input("Do you want to specify the length? (y/n): ")
    if length_check == "y":
        length = int(input("Enter the length of the password to be generated: "))
    else:
        length = int(random.randrange(4, 16))

    caps_check = input("Do you want capital letters in the password? (y/n): ")
    if caps_check == "y":
        caps = True
    else:
        caps = False
    
    number_check = input("do you want numbers in the password? (y/n): ")
    if number_check == "y":
        numbers = True
    else:
        numbers = False

    symbol_check = input("do you want symbols in the password? (y/n): ")
    if number_check == "y":
        symbols = True
    else:
        symbols = False

    password = Password(length, caps, numbers, symbols)
    print("Your password is: " + password)
    
main()
