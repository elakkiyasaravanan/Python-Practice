text=input("Enter a string: ")
count=0
for i in text:
  if i in "0123456789":
    count+=1
print(count)

#OR

text=input("Enter a string: ")
count=0
for i in text:
  if i.isdigit():
    count+=1
print(count)
