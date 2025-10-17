text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print("Modified string:", result)
