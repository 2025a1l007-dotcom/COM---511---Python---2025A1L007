# write a python program take a  student name and roll number , then generate a username using the first 3 letter of the name and the name and last 2 digits of the roll number

name = input("Enter name: ")
roll = input("Enter roll number: ")

username = name[ :3] + roll[ -2: ]

print("Generated  using name ")