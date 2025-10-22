n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
total = 0
count = 0
for num in numbers:
    total += num
    count += 1

if count > 0:
    avg = total / count
    print("Average of elements:", avg)
else:
    print("List is empty!")
