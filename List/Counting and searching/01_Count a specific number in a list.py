n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

search = int(input("Enter the number to count: "))

count = 0

for i in numbers:
    if i == search:
        count += 1

print(f"{search} appears {count} time(s) in the list.")
