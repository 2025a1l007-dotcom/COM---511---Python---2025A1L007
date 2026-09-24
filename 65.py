#write a python program to store all month names in atuple .Input a month number and display the corrresponding month name.# Store all month names in a tuple
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Input month number
month_number = int(input("Enter month number (1-12): "))

# Display corresponding month name
if 1 <= month_number <= 12:
    print("Month:", months[month_number - 1])
else:
    print("Invalid month number")
