n=int(input("Enter n: "))
number=[]
for i in range(n):
      num=int(input(f"Enter value {i+1}: "))
      number.append(num)
pro=1
for i in number:
      if i%2==0:
          pro*=i
      
print("Product of Even number is: ",pro)
