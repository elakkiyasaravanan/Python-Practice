text = input("Enter a string: ")
text = text.lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in text:
    if char.isalpha():  # Check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
