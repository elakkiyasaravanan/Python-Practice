n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i

if largest % smallest == 0:
    print("Largest is a multiple of smallest.")
else:
    print("Largest is not a multiple of smallest.")
