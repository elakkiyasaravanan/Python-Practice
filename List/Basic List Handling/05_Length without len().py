n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

count = 0
for num in numbers:
    count += 1

print("Length of the list:", count)
