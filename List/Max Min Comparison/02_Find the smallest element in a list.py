n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest element:", smallest)
