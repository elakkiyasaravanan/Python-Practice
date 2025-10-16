text = input("Enter a string: ")
search = input("Enter a character to check: ")

if len(text) == 0:
    print("String is empty.")
else:
    if text.startswith(search):
        print(f"The string starts with '{search}'.")
    else:
        print(f"The string does not start with '{search}'.")

    if text.endswith(search):
        print(f"The string ends with '{search}'.")
    else:
        print(f"The string does not end with '{search}'.")
