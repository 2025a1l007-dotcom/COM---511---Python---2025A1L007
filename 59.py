numbers = []
even = []
odd = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Original List:", numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
