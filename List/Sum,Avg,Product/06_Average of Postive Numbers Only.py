n=int(input("Enter n : "))
empty=[]
sum=0
count=0
for i in range(n):
  num=int(input(f"Enter number {i+1} : "))
  empty.append(num)
for i in empty:
  if i>0:
    sum+=i
    count+=1
if count > 0:
    avg = sum / count
    print("Average of Positive Numbers is:", avg)
else:
    print("No positive numbers in the list.")
