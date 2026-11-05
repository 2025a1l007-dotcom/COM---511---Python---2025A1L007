def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


def armstrong(n):
    temp = n
    power = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10

    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number:", max_of_three(a, b, c))

n = int(input("Enter a number: "))
armstrong(n)

