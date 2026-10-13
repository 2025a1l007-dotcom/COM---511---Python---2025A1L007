#write a program to perform searching activity using linear and binary search
# Linear and Binary Search

a = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter number to search: "))

# Linear Search
found = False

for i in range(len(a)):
    if a[i] == key:
        print("Linear Search: Found at position", i + 1)
        found = True
        break

if not found:
    print("Linear Search: Not Found")


# Binary Search
a.sort()
low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Binary Search: Found at position", mid + 1)
        found = True
        break
    elif key < a[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print("Binary Search: Not Found")