m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

avg = (m1 + m2 + m3) / 3

# Checks if each mark is at least 40 AND the average is at least 50
result = (m1 >= 40) and (m2 >= 40) and (m3 >= 40) and (avg >= 50)
print(result)