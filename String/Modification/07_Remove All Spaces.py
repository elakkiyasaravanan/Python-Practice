# Method 1: Using .replace()
text = input("Enter a string: ")
text_no_spaces = text.replace(" ", "")
print("Without spaces:", text_no_spaces)

# Method 2: Using a loop
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch != " ":
        result += ch
print("Without spaces:", result)
