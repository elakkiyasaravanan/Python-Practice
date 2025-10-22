n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

print("Sum of elements:", total)
