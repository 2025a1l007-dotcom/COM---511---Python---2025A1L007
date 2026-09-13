while True:
    password = input("Enter your password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted")
        break
    else:
        print("weak password. Try again")
