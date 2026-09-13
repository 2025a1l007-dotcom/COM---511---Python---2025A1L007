correct_pin = "1234"

while True:
    pin = input("Enter your 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Error: PIN must contain exactly 4 digits.")
        continue

    if pin == correct_pin:
        print("Lock opened!")
        break
    else:
        print("Incorrect PIN. Please try again.")