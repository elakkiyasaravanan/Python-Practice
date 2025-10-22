text = input("Enter a string: ")

words = text.split()
unique_words = []

for word in words:
    if word not in unique_words:     
        unique_words.append(word)

result = ' '.join(unique_words)
print("After removing duplicates:", result)
