#first way
n = int(input("Enter a number: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print(n, "is prime")
else:
    print(n, "is not prime")
  
#second way
n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")
