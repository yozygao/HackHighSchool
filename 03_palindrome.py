word = input("Enter the text which may be a palindrome: ").lower()
rev_word = word[::-1]
if word==rev_word:
    print("It is a palindrome!. So cool!")
else:
    print("It's not a palindrome. Boohoo.")

