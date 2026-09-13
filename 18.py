#write a python program to take a word and count the number and count the number of vowels a,e ,i,o,u.
word = input("Enter a  word: ")

count = 0

for ch in word:
    if ch.lower() in "aeiou":
       count += 1

print("Number of vowels:", count)