data=input("Enter elements: ").split()
t=tuple(map(int,data))
count=0;
for i in t:
  if i%2==0:
    count+=1
print("Total Even Numbers: ",count)
