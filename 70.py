#write a python program to store multiple student records as a list of tuples.each tuple shouls contain name, roll no,and marks.Display students who scored above 75.
students = [
    ("Rahul", 101, 85),
    ("Aman", 102, 65),
    ("Priya", 103, 90),
    ("Neha", 104, 72),
    ("Ravi", 105, 80)
]

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print(student)

