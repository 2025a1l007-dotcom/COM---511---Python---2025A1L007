bill = float(input("Enter the total bill amount: "))

if bill > 5000:
    discount = bill * 20 / 100
elif bill >= 3000:
    discount = bill * 10 / 100
else:
    discount = 0

final_bill = bill - discount

print("Discount amount:", discount)
print("Final bill amount:", final_bill)

