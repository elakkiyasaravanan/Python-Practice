text = input("Enter a string: ")
result = ""
seen = {}  

for ch in text:
    if ch not in seen:  
        result += ch
        seen[ch] = True  

print("String without duplicates:", result)
