#write a python program to take a word and print it in reverse order using slicing .Also check wheather it id the same forward and backward.
word = input("enter a word: ")

reverse = word[::-1]

print("Reverse:", reverse)

if word == reverse:
    print("It is a palidrome")
else:
    print("It is not a palidrome")