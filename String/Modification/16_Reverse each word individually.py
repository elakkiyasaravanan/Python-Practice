text = input("Enter a string: ")

words = text.split()               
reversed_each = [word[::-1] for word in words] 
result = ' '.join(reversed_each)

print("Each word reversed:", result)
