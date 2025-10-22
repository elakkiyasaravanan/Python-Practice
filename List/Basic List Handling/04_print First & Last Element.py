n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

if numbers: 
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])
else:
    print("List is empty!")
