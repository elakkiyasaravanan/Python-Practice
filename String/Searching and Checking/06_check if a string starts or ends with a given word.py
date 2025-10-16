# manual way

text = input("Enter a string: ")
word_start = input("Enter the word to check at start: ")
word_end = input("Enter the word to check at end: ")

# Check start using slicing
if text[:len(word_start)] == word_start:
    print(f"The string starts with '{word_start}'.")
else:
    print(f"The string does not start with '{word_start}'.")

# Check end using slicing
if text[-len(word_end):] == word_end:
    print(f"The string ends with '{word_end}'.")
else:
    print(f"The string does not end with '{word_end}'.")
