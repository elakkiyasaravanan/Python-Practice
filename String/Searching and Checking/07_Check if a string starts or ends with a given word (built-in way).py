# built-in way

text = input("Enter a string: ")
word_start = input("Enter the word to check at start: ")
word_end = input("Enter the word to check at end: ")

if text.startswith(word_start):
    print(f"The string starts with '{word_start}'.")
else:
    print(f"The string does not start with '{word_start}'.")

if text.endswith(word_end):
    print(f"The string ends with '{word_end}'.")
else:
    print(f"The string does not end with '{word_end}'.")
