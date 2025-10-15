text = input("Enter a string: ")
special_count = 0
for i in text:
    if not i.isalpha() and not i.isdigit():  
        special_count += 1
print("Number of special characters:", special_count)
