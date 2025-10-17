text=input("Enter a string: ")
if len(text) >= 2:
    text = text[-1] + text[1:-1] + text[0]
print("Swapped string:", text)
