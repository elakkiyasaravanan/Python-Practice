# Method 1: Slicing
text=input("Enter a String: ")
reverse = text[::-1]
print(reverse)

# Method 2: Using Loop
text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  
print("Reversed string:", reversed_text)
