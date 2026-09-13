#take student full name and roll no..Generate email using first 3 letters of first name, first 3 letters of last name ,and last 3 characters of roll no
name = input("Enter student's full name: ")
roll_no = input("Enter roll number: ")

# Split the name into first and last name
parts = name.split()

first_name = parts[0]
last_name = parts[-1]

# Generate email
email = first_name[:3].lower() + last_name[:3].lower() + roll_no[-3:] + "@gmail.com"

print("Generated Email:", email)