a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
min_num = min(a, b)
for i in range(min_num, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

print("GCD is", gcd)
