import json

# Run for the first time. 

with open('.passwords.json') as f:
    passwords = json.load(f)

print("Welcome to Drac's PasswordManager. ")
print("You will be setting up your master password right now. ")

print("\nPlease enter your new master password. Be sure to remember it. ")
new_master_password = input(">")

print("Great, we'll set this up quickly. ")

passwords["master"] = new_master_password
with open(".passwords.json", "w") as outfile:
    json.dump(passwords, outfile)