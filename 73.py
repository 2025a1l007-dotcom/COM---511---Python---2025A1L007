# Small Library Management System

library = {}

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")

        if book in library:
            print("Book already exists.")
        else:
            library[book] = "Available"
            print("Book added successfully.")

    elif choice == "2":
        book = input("Enter book name to issue: ")

        if book not in library:
            print("Book not found.")
        elif library[book] == "Issued":
            print("Book is already issued.")
        else:
            library[book] = "Issued"
            print("Book issued successfully.")

    elif choice == "3":
        book = input("Enter book name to return: ")

        if book not in library:
            print("Book not found.")
        elif library[book] == "Available":
            print("Book is already available.")
        else:
            library[book] = "Available"
            print("Book returned successfully.")

    elif choice == "4":
        print("\n--- Current Book Records ---")

        if not library:
            print("No books in the library.")
        else:
            for book, status in library.items():
                print(f"{book} : {status}")

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
