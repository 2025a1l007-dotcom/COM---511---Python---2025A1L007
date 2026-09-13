# Take an email address and check whether it contains @ and .com
email = input("Enter your email address: ")

if "@" in email and ".com" in email:
    print("Valid email")
else:
    print("Invalid email")
