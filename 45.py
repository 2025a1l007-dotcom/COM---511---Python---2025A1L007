# write a python program to input a decimal number and convert it into binary without using the bult -in bin() function# Input a decimal number
num = int(input("Enter a decimal number: "))

# Handle zero separately
if num == 0:
    print("Binary: 0")
else:
    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print("Binary:", binary)
