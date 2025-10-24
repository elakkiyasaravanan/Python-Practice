n=int(input("How many numbers: ")) 
numbers=[int(input(f"Enter value {i+1}: ")) for i in range(n)] 
largest=numbers[0] 
smallest=numbers[0] 
for i in numbers: 
    if i>largest: 
      largest=i 
    elif i<smallest: 
      smallest=i
total=largest+smallest
avg=total/2
print("Average of largest and smallest numbers in list is: ",avg)
