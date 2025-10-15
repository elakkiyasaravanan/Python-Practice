text=input("Enter a string: ")
vowel="aeiouAEIOU"
count=0
for i in text:
  if i in vowels:
    count+=1
print("Number of vowels:", count)
