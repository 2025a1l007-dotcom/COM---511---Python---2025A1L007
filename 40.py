# Write a python program that asks the user to enter a username and password .The user should get only 3 attempts .If the correct credentails are entered ,display"Login Successful"and stop the loop.If all attempts are used,display"Account Locked".
correct_username = "admin"
correct_password = "1234"

for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")

