#write a python program to allocate seats to a group in a single row of a cinema hall .First , input the total number of seats n.Then enter the status of each seat.
n = int(input("Enter the total number of seats: "))

seats = []

print("Enter seat status (0 = vacant, 1 = occupied):")
for i in range(n):
    status = int(input(f"Seat {i + 1}: "))
    seats.append(status)

group = int(input("Enter the number of seats required for the group: "))

# Find consecutive vacant seats
found = False

for i in range(n - group + 1):
    if all(seats[j] == 0 for j in range(i, i + group)):
        print("Seats allocated:", end=" ")
        for j in range(i, i + group):
            seats[j] = 1
            print(j + 1, end=" ")
        found = True
        break

if not found:
    print("Sorry, consecutive seats are not available.")

print("\nUpdated seat status:")
print(seats)
