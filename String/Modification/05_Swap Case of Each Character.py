text=input("Enter a string: ")
result = ""
for ch in text:
    if ch.islower():
        result += ch.upper()
    else:
        result += ch.lower()
print(result)
