def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = int(input("Enter your choice: "))

match ch:
    case 1:
        print("Result:", add(a, b))
    case 2:
        print("Result:", subtract(a, b))
    case 3:
        print("Result:", multiply(a, b))
    case 4:
        if b != 0:
            print("Result:", divide(a, b))
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid choice")