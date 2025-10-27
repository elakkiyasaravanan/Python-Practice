n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

positive_count = 0
negative_count = 0
zero_count = 0

for i in numbers:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
    elif i == 0:
        zero_count += 1

print("Positive numbers count:", positive_count)
print("Negative numbers count:", negative_count)
print("Zero count:", zero_count)
