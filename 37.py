for i in range(1, 6):
    marks = float(input("Enter marks for student " + str(i) + ": "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
        continue

    print("Marks are valid:", marks)
