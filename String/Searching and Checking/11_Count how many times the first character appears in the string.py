text = input("Enter a string: ")

if len(text) == 0:
    print("Empty string")
else:
    first_char = text[0]
    count = 0

    for char in text:
        if char == first_char:
            count += 1

    print(f"The first character '{first_char}' appears {count} times in the string.")
