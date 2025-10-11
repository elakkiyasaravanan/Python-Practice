text = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_text = ""
for char in text:
    if char in vowels:
        new_text += "*"
    else:
        new_text += char

print("After replacing vowels:", new_text)
