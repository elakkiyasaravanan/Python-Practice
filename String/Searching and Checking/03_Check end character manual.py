text = input("Enter a string: ")
search = input("Enter a character to check end: ")

if text[-1] == search:
    print("Yes, the string ends with", search)
else:
    print("No, the string does not end with", search)
