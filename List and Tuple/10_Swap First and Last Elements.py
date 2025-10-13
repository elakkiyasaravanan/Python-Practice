n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Swap first and last
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping first and last elements:", numbers)
