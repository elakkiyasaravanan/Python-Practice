n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

print("Elements between smallest and largest (value-wise):")

for i in numbers:
    if smallest < i < largest:
        print(i, end=" ")
