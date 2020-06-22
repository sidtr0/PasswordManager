import json
import time

with open('.passwords.json') as f:
    passwords = json.load(f)

print("Password file detecting... \n")
time.sleep(2.0)
print("File detected. You may now use the password manager. \n\n")

print("Enter your master password so that I know you are authorized. ")
test_for_master = input(">")

if test_for_master == passwords["master"]:
    pass
else:
    print("Unsuccesful. Terminating attempt. Try again. ")
    exit(0)

print("Commands: ")
print("show - use this to see one of your passwords. ")
print("add - use this to add another password to the list. ")
print("exit - exit the password manager. ")
print("help - will print out this text containing info on all commands. \n")

while True:
    choice_of_command = input("Enter a command. \n>")

    if choice_of_command == "show":
        site_to_see = input("Which site's password would you like to see? \n>")
        if site_to_see in passwords:
            print(f"{site_to_see}'s password: ")
            print(f"{passwords[site_to_see]}")
        else: 
            print("You don't have any site with that name. ")
            pass

    elif choice_of_command == "add":
        new_website_name = input("What is the name of the website you would like to add? \n(Recommendation: don't put the entire website name, just the main part. Ex: \"discord\" instead of \"discord.com\") \n>")
        new_website_password = input("Enter the password for the new website: ")
        new_website = {f"{new_website_name}": f"{new_website_password}"}
        passwords.update(new_website)

        with open(".passwords.json", "w") as outfile:
            json.dump(passwords, outfile)

    elif choice_of_command == "exit":
        break

    elif choice_of_command == "help":
        print("Commands: ")
        print("show - use this to see one of your passwords. ")
        print("add - use this to add another password to the list. ")
        print("exit - exit the password manager. ")
        print("help - will print out this text containing info on all commands. \n")

    else:
        print("Couldn't recognize command. Please try again")