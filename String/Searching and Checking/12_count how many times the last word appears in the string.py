text = input("Enter a string: ")

# Check if empty
if len(text.strip()) == 0:
    print("Empty string")
else:
    words = text.split()        
    last_word = words[-1]        
    count = 0

    for w in words:
        if w == last_word:
            count += 1

    print(f"The last word '{last_word}' appears {count} times.")
