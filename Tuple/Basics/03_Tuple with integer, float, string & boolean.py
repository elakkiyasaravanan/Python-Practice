i = int(input("Enter an integer: "))
f = float(input("Enter a float value: "))
s = input("Enter a string: ")

b = input("Enter True/False: ")
b = True if b == "True" else False

t = (i, f, s, b)
print("Tuple with mixed data types:", t)
