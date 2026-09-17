numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Original List:", numbers)

# Rotate one position to the right
last = numbers.pop()
numbers.insert(0, last)

print("List after right rotation:", numbers)
