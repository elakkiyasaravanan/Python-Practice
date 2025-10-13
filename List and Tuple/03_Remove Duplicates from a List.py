n=int(input("enter number of elements: "))
numbers=[]
for i in range(n):
  num=int(input(f"Enter elements {i+1} : "))
  numbers.append(num)
unique=[]
for num in numbers:
  if num not in unique:
    unique.append(num)
print("List after removing duplicates:", unique)
