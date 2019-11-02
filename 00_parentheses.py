x = input("Enter a word here: ")
def foo(s):
    ret = ""
    i = True
    for char in s:
        if i:
            ret += char.lower()
        else:
            ret += char.upper()
        if char != ' ':
            i = not i
    return ret

def replace_vowel(s):
    word = foo(x)
    vowels = ("A", "E", "I", "O", "U")
    for vowels in vowels:
       word = word.replace(vowels, "*")
    return word 

def check_parentheses(s):
    word = foo(x)
    if word.count("(") == word.count(")"):
        print("Balanced? True.")
    else:
        print("Balanced? False.")
    return ""
print (foo(x))
print (replace_vowel(x))
print(check_parentheses(x))
