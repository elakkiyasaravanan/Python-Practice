# Method 1: User gives which character to check
text = "Elakkiya"
ch = "a"

count = 0
for i in text:
    if i == ch:
        count += 1

print(f"'{ch}' appears {count} times in the string.")


# Method 2: Count all character frequencies
text = "Elakkiya"
freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for char, count in freq.items():
    print(char, ":", count)
