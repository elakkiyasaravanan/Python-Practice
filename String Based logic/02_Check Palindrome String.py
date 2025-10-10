text=input("Enter a String: ")
text_lower=text.lower()
reverse =text_lower[::-1]
if text_lower==reverse:
  print("palindrome")
else:
  print("Not palindrome ")
