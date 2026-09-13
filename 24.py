#write a python program to  take a password and check wheather it contains @ and has at least 8 characters.
password = input("Enter your password: ")

if "@" in password and len(password) >= 8:
    print("Valid password")
else:
    print("Invalid password")