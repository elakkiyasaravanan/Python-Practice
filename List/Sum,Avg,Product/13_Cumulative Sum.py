n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

cumulative_sum = []
total = 0

for num in numbers:
    total += num        
    cumulative_sum.append(total)  

print("Original List:", numbers)
print("Cumulative Sum List:", cumulative_sum)
