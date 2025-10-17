text = input("Enter a string: ")
result = ""

for ch in text:
    if ch in vowels:   
        result += ch       

print("String without vowels:", result)
