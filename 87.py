import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:

    sides = sorted([a, b, c])

    if math.isclose(sides[0]**2 + sides[1]**2,
                    sides[2]**2):
        print("Right angled triangle")
    else:
        print("Not a right angled triangle")

    s = (a + b + c) / 2

    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("Area:", area)

else:
    print("Invalid triangle")