name = input("Enter your name: ")
branch = input("Enter your branch: ")
year = input("Enter your year: ")

code_name = name[:3] + branch[:3] + year[-1] * 2

print("Code Name:", code_name)