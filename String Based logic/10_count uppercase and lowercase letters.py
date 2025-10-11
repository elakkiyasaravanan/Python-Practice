text=input("Enter a string: ")
upper_count=0
lower_count=0
for i in text:
  if i.isupper():
    upper_count+=1
  elif i.islower():
    lower_count+=1
print(f"UpperCase Letters: {upper_count} LowerCase Letters: {lower_count}")
