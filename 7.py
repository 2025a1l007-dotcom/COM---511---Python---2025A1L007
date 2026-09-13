name = str(input("Enter name: "))
roll_number = int(input("Enter roll number: "))
cgpa = float(input("Enter CGPA: "))
# Enter True/False or 1/0 for hostel status
hostel_status = bool(input("Enter hostel status (leave blank for False, type anything for True): "))

print(f"Name: {name}, Type: {type(name)}")
print(f"Roll Number: {roll_number}, Type: {type(roll_number)}")
print(f"CGPA: {cgpa}, Type: {type(cgpa)}")
print(f"Hostel Status: {hostel_status}, Type: {type(hostel_status)}")