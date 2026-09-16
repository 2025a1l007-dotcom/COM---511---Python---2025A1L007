numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers = list(set(numbers))
numbers.sort()

if len(numbers) >= 2:
    print("Second largest number:", numbers[-2])
else:
    print("Second largest number does not exist.")