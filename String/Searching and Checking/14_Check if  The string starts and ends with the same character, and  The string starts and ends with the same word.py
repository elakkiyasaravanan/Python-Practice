text = input("Enter a string: ")

#  Remove any extra spaces (important)
text = text.strip()

#  Character comparison (start & end)
if text[0].lower() == text[-1].lower():  # ignore case
    print("String starts and ends with the same character.")
else:
    print("Characters are different.")

#  Split into words
words = text.split()

#  Word comparison (start & end)
if len(words) > 1 and words[0].lower() == words[-1].lower():
    print("String starts and ends with the same word.")
else:
    print("Words are different.")
