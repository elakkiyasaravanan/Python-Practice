data = input("Enter characters separated by space: ").split()
t = tuple(data)
count = 0
for ch in t:
    if ch.isupper():
        count += 1

print("Total uppercase letters:", count)
