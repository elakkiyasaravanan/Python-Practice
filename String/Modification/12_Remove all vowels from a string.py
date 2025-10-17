text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in vowels:    
        result += ch        

print("String without vowels:", result)
