text=input("Enter a string: ")
vowel="aeiouAEIOU"
count=0
for i in text:
  if i.isalpha() and i not in vowel:
    count+=1
print("Number of Consonants:", count)
