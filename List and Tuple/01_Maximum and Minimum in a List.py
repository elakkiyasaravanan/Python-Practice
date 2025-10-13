n=int(input("Enter number of elements: " ))
numbers=[]
for i in range(n):
  num=int(input("Enter Elements: "))
  numbers.append(num)
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Maximum number:", max_num)
print("Minimum number:", min_num)
