n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)
