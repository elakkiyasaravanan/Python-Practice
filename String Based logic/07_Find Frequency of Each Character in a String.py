text = input("Enter a string: ")

freq = {}  # empty dictionary

for char in text:
    if char in freq:
        freq[char] += 1  # already exists, increase count
    else:
        freq[char] = 1   # first occurrence

# Print frequency
for char, count in freq.items():
    print(char, ":", count)
