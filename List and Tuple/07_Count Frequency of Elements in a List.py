n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key, value in freq.items():
    print(f"{key} appears {value} times")
