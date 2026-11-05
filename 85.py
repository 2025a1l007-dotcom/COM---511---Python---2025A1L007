class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


e1 = Employee("Riya", 101, 25000)
e2 = Manager("Rahul", 102, 50000, "IT")

print("Employee Details:")
e1.display()

print("\nManager Details:")
e2.display()