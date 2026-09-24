#write a python program to store repeated values in a tuple and count hoe many times a given value appears.
numbers = (10, 20, 10, 30, 20, 10, 40, 20)


value = int(input("Enter the value to count: "))


occurrences = numbers.count(value)

print("Tuple:", numbers)
print(value, "appears", occurrences, "times.")
