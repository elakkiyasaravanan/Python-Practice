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

common = []
for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)
