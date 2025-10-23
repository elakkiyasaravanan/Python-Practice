n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize sums
sum1 = 0
sum2 = 0

# First half sum
for i in range(n // 2):
    sum1 += numbers[i]

# Second half sum
for i in range(n // 2, n):
    sum2 += numbers[i]

# Averages
avg1 = sum1 / (n // 2)
avg2 = sum2 / (n - n // 2)

print("Average of first half:", avg1)
print("Average of second half:", avg2)
