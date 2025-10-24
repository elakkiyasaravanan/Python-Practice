n = int(input("How many numbers? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

second_largest = float('-inf')
for num in numbers:
    if num != largest and num > second_largest:
        second_largest = num

print("Second largest element:", second_largest)
