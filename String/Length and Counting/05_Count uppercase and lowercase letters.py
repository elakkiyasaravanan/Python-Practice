text=input("Enter a string: ")
up_count=0
low_count=0
for i in text:
  if i.isupper():
    up_count+=1
  elif i.islower():
    low_count+=1
print("Uppercase Count: ",up_count)
print("Lowercase Count: ",low_count)

