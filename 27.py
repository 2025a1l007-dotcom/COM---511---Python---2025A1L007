#take a sentence containg double spaces and unwanted spaces at the beginning orvend .clean the sentence.
sentence = input("Enter a sentence: ")

semtence = sentence.strip()
sentence = sentence.replace("  ","")

print("Clean sentence:", sentence)