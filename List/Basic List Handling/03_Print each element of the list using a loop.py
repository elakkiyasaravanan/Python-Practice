n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nNumbers in the list:")
for num in numbers:
    print(num)
