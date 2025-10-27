n = int(input("How many numbers: "))
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

search = int(input("Enter the number to find index of: "))
index = -1   

for i in range(len(numbers)):
    if numbers[i] == search:
        index = i     
        break          

if index != -1:
    print(f"{search} found at index {index}")
else:
    print(f"{search} not found in the list")
