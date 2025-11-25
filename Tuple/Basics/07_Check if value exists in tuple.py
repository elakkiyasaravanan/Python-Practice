data = input("Enter elements: ").split()
t = tuple(data)
val = input("Enter value to check: ")
if val in t:
    print("Value exists in the tuple")
else:
    print("Value not found")
