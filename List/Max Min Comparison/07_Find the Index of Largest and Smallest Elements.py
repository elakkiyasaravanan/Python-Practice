n=int(input("How many numbers: "))
numbers=[int(input(f"Enter value {i+1}: ")) for i in range(n)]
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if i>largest:
       largest=i
    elif i<smallest:
       smallest=i
index_largest=numbers.index(largest)
index_smallest=numbers.index(smallest)
print("Index of largest number is: ",index_largest)
print("Index of smallest number is: ",index_smallest)
