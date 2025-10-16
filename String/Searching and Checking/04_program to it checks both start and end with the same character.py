text = input("Enter a string: ")
search = input("Enter a character to check: ")

# Check for empty string first
if len(text) == 0:
    print("String is empty.")
else:
    # Check start
    if text[0] == search:
        print(f"The string starts with '{search}'.")
    else:
        print(f"The string does not start with '{search}'.")

    # Check end
    if text[-1] == search:
        print(f"The string ends with '{search}'.")
    else:
        print(f"The string does not end with '{search}'.")
