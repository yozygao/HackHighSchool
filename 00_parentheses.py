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
def parentheses_check(s):
    stack = foo(x)
    for line in s:
        for c in line:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack[-1] != '(':
                    print("Balanced? False.")
                else:
                    print("Balanded? True.")
print (foo(x))
print(replace_vowel(x))
print(parentheses_check(x))
