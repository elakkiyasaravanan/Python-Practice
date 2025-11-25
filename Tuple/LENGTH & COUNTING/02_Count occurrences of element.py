data=input("Enter Elements: ").split()
t=tuple(map(int,data))
search=int(input("Enter Element To search: "))
count=0
for i in t:
  if i==search:
    count+=1
print("Count : ",count)
