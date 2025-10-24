n=int(input("How many Numbers"))
numbers=[int(input(f"Enter value {i+1} : ")) for i in range(n)]
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
  if i>largest:
    largest=i
  elif i<smallest:
    smallest=i
diff=largest-smallest
print("Difference between largest and smallest is: ",diff)
