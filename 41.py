#write a python program to input a number and check weather it is prime if it has no divisor other than1 and itself.num = int(input("Enter a number: "))
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


