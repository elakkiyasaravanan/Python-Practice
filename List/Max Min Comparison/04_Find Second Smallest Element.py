n = int(input("How many numbers? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

second_smallest = float('inf') 
for num in numbers:
    if num != smallest and num < second_smallest:
        second_smallest = num

print("Second smallest element:", second_smallest)
