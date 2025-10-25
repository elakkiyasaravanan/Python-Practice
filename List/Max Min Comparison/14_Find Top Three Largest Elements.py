n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

first = second = third = float('-inf')

for num in numbers:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != second and num != first:
        third = num

# Check if we found 3 distinct numbers
if third == float('-inf'):
    print("Less than 3 distinct numbers in the list.")
else:
    print("Top 3 largest numbers are:", first, second, third)
