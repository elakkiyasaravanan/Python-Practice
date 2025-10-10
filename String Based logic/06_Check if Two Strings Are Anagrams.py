# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Sort letters
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")
