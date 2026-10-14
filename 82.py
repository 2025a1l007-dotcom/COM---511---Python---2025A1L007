# Write  a python program that allow a librarian to add several books to a library.For each book, ask the user to enter its title and the number of copies .Store each book and its avaliable copy  count in a dictionary.
library = {}


n = int(input("Enter the number of books to add: "))

for i in range(n):
    title = input("Enter book title: ")
    copies = int(input("Enter number of copies: "))
    library[title] = copies


while True:
    print("\n--- Library Menu ---")
    print("1. Issue a book")
    print("2. Return a book")
    print("3. Display all books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title to issue: ")

        if title in library and library[title] > 0:
            library[title] -= 1
            print("Book issued successfully!")
        elif title in library:
            print("No copies available.")
        else:
            print("Book not found.")

    elif choice == "2":
        title = input("Enter book title to return: ")

        if title in library:
            library[title] += 1
            print("Book returned successfully!")
        else:
            print("Book not found in library.")

    elif choice == "3":
        print("\nBooks in Library:")
        for title, copies in library.items():
            print(title, ":", copies, "copies available")

    elif choice == "4":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
