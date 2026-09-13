password = input("Enter your password: ")

length_check = len(password) >= 8
at_check = "@" in password
different_check = password[0] != password[-1]

print("Length is at least 8:", length_check)
print("Contains @:", at_check)
print("First and last characters are different:", different_check)