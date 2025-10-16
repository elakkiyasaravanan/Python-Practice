text = input("Enter a string: ")

if len(text) == 0:
    print("Empty string")
else:
    freq = {}

    # count frequency
    for ch in text:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1

    # find most frequent character
    most_freq_char = max(freq, key=freq.get)

    # compare with first character
    if text[0] == most_freq_char:
        print(f"Starts with most frequent character '{most_freq_char}'")
    else:
        print(f"Does not start with most frequent character '{most_freq_char}'")

    print("Character frequencies:", freq)
