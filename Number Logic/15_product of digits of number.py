N = int(input("Enter a number: "))
Total =1
While N>0:
Digit=N%10
Total *=Digit
N=N//10
Print(Total)
