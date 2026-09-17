list1 = []
list2 = []
common = []

n1 = int(input("Enter the number of elements in first list: "))

for i in range(n1):
    num = int(input("Enter an element: "))
    list1.append(num)

n2 = int(input("Enter the number of elements in second list: "))

for i in range(n2):
    num = int(input("Enter an element: "))
    list2.append(num)

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("First List:", list1)
print("Second List:", list2)
print("Common Elements:", common)
