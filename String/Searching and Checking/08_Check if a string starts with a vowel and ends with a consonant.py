text = input("Enter a string: ")
vowels = "aeiouAEIOU"

# Check start
if len(text) == 0:
    print("Empty string")
else:
    if text[0] in vowels:
        print("String starts with a vowel")
    else:
        print("String does not start with a vowel")
    
    # Check end
    if text[-1].isalpha() and text[-1] not in vowels:
        print("String ends with a consonant")
    else:
        print("String does not end with a consonant")
