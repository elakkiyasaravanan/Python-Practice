data = input("Enter strings separated by space: ").split()
t = tuple(data)
count = 0
for s in t:
    if len(s) > 5:
        count += 1
print("Strings with length > 5:", count)
