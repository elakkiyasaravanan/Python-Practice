n=int(input("Enter a number: "))
num=n
rev=0
while n>0:
  digit=n%10
  rev=rev*10+digit
  n=n//10
if num==rev:
  print(original, "is a palindrome")
else:
  print(original, "is not a palindrome")
