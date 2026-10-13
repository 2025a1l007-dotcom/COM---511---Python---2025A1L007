#create a class and object: Student details

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)

# Create an object
s1 = Student("Tanvi", 101)

# Display student details
s1.display()
