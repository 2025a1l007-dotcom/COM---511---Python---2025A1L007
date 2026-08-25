## Input the amount in rupees
amount = int(input("Enter the amount in rupees: "))

# Calculate the number of 500 rupee notes
notes_500 = amount // 500

# Calculate remaining amount after using 500 rupee notes
remaining_amount = amount % 500

# Calculate the number of 100 rupee notes from the remaining amount
notes_100 = remaining_amount // 100

print(f"Number of 500 rupee notes needed: {notes_500}")
print(f"Number of 100 rupee notes needed: {notes_100}")
