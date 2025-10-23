n=int(input("Enter n : "))
numbers=[]
for i in range(n):
  num=int(input("Enter values: "))
  numbers.append(num)
product = 1
for i in range(len(numbers)):   
    if i % 2 == 0:               
        product *= numbers[i]   
print("Product of numbers at even index positions:", product)
