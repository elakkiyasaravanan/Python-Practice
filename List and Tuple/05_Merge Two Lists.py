n1 = int(input("Enter number of elements in first list: "))
list1 = []
for i in range(n1):
    num = int(input(f"Enter element {i+1} of first list: "))
    list1.append(num)

n2 = int(input("Enter number of elements in second list: "))
list2 = []
for i in range(n2):
    num = int(input(f"Enter element {i+1} of second list: "))
    list2.append(num)

# Merge manually
merged = []
for num in list1:
    merged.append(num)
for num in list2:
    merged.append(num)

print("Merged list:", merged)
