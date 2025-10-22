text = input("Enter a string: ")

words = text.split()         
reversed_words = words[::-1]  
result = ' '.join(reversed_words)

print("Reversed words:", result)
