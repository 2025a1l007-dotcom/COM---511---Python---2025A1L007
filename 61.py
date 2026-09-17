cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == 3:
        print("Your Cart:", cart)

    elif choice == 4:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
