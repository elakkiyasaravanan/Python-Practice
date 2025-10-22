# build in method
text = input("Enter a string: ")
result = text.title()
print("Title case string:", result)


#Manual method 
text = input("Enter a string: ")

words = text.split()       
result = ""

for word in words:
    capitalized = word[0].upper() + word[1:].lower()
    result += capitalized + " "

print("Title case string:", result.strip())
