#write a python progrm to input a student's marks in n consecutive tests and store them in a list .Find the longest consecutive sequence in which each mark is strictly greater than the previous mark
n = int(input("Enter number of tests: "))

marks = []

for i in range(n):
    mark = int(input("Enter marks for test " + str(i + 1) + ": "))
    marks.append(mark)

longest = []
current = []

for i in range(n):
    if i == 0 or marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        if len(current) > len(longest):
            longest = current.copy()
        current = [marks[i]]

# Check the last sequence
if len(current) > len(longest):
    longest = current.copy()

print("Marks:", marks)
print("Longest consecutive increasing sequence:", longest)
print("Length:", len(longest))


