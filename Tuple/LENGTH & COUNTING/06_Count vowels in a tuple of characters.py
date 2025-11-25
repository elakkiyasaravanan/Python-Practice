data = input("Enter characters separated by space: ").split()
t = tuple(data)
vowels = "aeiouAEIOU"
count = 0
for ch in t:
    if ch in vowels:
        count += 1
print("Total vowels:", count)
