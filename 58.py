numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Create a new list containing only unique elements
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Display the new list
print("Unique elements:", unique_numbers)
