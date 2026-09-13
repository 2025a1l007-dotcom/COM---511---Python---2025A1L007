cgpa = float(input("Enter your CGPA: "))
attendance = float(input("Enter your attendance percentage: "))

national_competition = input("Have you won a national-level competition? (yes/no): ")

if (cgpa >= 8.5 and attendance >= 85) or national_competition.lower() == "yes":
    print("Student is eligible for scholarship.")
else:
    print("Student is not eligible for scholarship.")