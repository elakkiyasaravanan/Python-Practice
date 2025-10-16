text = input("Enter a string: ").strip()
word = input("Enter a word: ").strip()
first_char = text[0]
last_char = text[-1]
if first_char in word or last_char in word:
    print("The string starts or ends with a character from the word.")
else:
    print("No match found.")
