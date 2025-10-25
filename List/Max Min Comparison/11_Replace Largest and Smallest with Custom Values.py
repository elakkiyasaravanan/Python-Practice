n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i


replace_largest = int(input("Enter value to replace largest: "))
replace_smallest = int(input("Enter value to replace smallest: "))

index_largest = numbers.index(largest)
index_smallest = numbers.index(smallest)

numbers[index_largest] = replace_largest
numbers[index_smallest] = replace_smallest

print("Updated list after replacement:", numbers)
