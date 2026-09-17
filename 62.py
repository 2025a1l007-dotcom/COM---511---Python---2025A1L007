numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter an element: "))
    numbers.append(num)

print("List:", numbers)

element = int(input("Enter the element to count: "))

count = numbers.count(element)

print("The element", element, "appears", count, "times.")
