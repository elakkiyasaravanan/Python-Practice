n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

sum_even = 0
sum_odd=0
for i in numbers:
    if i % 2 == 0:
      sum_even += i
    else:
      sum_odd+=i
diff=sum_even-sum_odd
print("Difference Between Sum of Even and Odd Numbers is : ",diff)
      


