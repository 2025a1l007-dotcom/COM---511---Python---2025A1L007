# Program to create and search student records

students = []

n = int(input("Enter number of students: "))

# Create student records
for i in range(n):
    print(f"\nEnter details of student {i + 1}:")

    while True:
        roll_no = input("Roll No.: ")

        # Check whether roll number is unique
        if any(student["roll_no"] == roll_no for student in students):
            print("Roll number already exists! Enter a unique roll number.")
        else:
            break

    name = input("Name: ")
    branch = input("Branch: ")
    marks = float(input("Marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

# Display all records
print("\n--- Student Records ---")
for student in students:
    print(student)

# Search for a student
search_roll = input("\nEnter roll number to search: ")

found = False

for student in students:
    if student["roll_no"] == search_roll:
        print("\nStudent Found!")
        print("Roll No.:", student["roll_no"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student with this roll number does not exist.")
