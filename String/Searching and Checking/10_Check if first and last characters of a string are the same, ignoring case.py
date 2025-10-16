text = input("Enter a string: ")

if len(text) == 0:
    print("Empty string")
elif text[0].lower() == text[-1].lower():
    print("First and last characters are the same (ignoring case)")
else:
    print("First and last characters are different")
