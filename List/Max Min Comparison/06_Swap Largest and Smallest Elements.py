n=int(input("How many Numbers"))
numbers=[int(input(f"Enter value {i+1} : ")) for i in range(n)]
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
  if i>largest:
    largest=i
  elif i<smallest:
    smallest=i
index_largest = numbers.index(largest) 
index_smallest = numbers.index(smallest) 
numbers[index_largest], numbers[index_smallest] = numbers[index_smallest], numbers[index_largest] 
print("List after swapping largest and smallest:", numbers)
