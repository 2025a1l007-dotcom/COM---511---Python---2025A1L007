comment = input("Enter your comment: ")

if ("make a lot of money" in comment.lower() or
    "buy now" in comment.lower() or
    "subscribe this" in comment.lower() or
    "click this" in comment.lower()):
    print("This comment is spam")
else:
    print("This comment is not spam")
