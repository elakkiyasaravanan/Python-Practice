text = input("Enter a string: ")
search = input("Enter a character to check start: ")

if text[0] == search:
    print("Yes, the string starts with", search)
else:
    print("No, the string does not start with", search)
