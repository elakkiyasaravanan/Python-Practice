text = input("Enter a string: ")
start_char = input("Enter the character to check at start: ")
end_word = input("Enter the word to check at end: ")

# Start check
if text[0] == start_char:
    print("Starts with", start_char)
else:
    print("Does not start with", start_char)

# End check
if text.endswith(end_word):
    print("Ends with", end_word)
else:
    print("Does not end with", end_word)
