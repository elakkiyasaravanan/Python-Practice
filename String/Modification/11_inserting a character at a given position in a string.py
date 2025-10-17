text = input("Enter a string: ")
char_to_insert = input("Enter a character to insert: ")
pos = int(input("Enter the position (index) to insert at: "))

new_text = text[:pos] + char_to_insert + text[pos:]
print("After insertion:", new_text)
