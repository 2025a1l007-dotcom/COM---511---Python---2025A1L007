#write a python program to store one student data as a tuple:name,rollno .,and marks.Display grade based on marks.name = input("Enter student name: ")
name = input("Enter student name: ")
rollno = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

student = (name, rollno, marks)

print("Student Data:", student)

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


