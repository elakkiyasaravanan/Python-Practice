n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
total = 0
for num in numbers:
    total += num
print("Sum of all elements:", total)
