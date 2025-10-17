text = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")

text = text.replace(char_to_remove, "")   # Replace with empty string

print("String after removal:", text)

# Manual Way
text = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")

result = ""
for ch in text:
    if ch != char_to_remove:   # only keep characters not matching
        result += ch

print("String after removal:", result)
