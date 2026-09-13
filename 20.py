#write a python program to take a sentence, detect double spaces,and repalace them with single spaces.
sentence = input("Enter a sentence: ")

if" " in sentence:
    print("Double spaces detected")
else:
    print("No double spaces")

sentence = sentence.replace(" "," ")

print("Updated sentence:",sentence)