roll = input("Enter roll number: ")

admission_year = roll[:4]
program_code = roll[4:7]
roll_digits = roll[-3:]

print("Admission Year:", admission_year)
print("Program Code:", program_code)
print("Roll No. Digits:", roll_digits)