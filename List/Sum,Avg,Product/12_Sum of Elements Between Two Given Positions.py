n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
start=int(input("Enter Starting index: "))
end=int(input("Enter Ending index: "))
sum=0
for i in range(start,end+1):
  sum+=numbers[i]
print("Sum of Elements Between Given Range: ",sum)
