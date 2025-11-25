data = input("Enter numbers separated by space: ").split()
t = tuple(map(int, data))
count = 0
for num in t:
    if num > 50:
        count += 1
print("Numbers greater than 50: ", count)
