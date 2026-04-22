text=input("enter the word")
print(text)
if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")