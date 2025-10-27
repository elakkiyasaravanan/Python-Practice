n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

search = int(input("Enter the number to search: "))

found = False

for i in numbers:
    if i == search:
        found = True
        break

if found:
    print(f"{search} is present in the list.")
else:
    print(f"{search} is not present in the list.")
