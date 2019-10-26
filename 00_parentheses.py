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
x = input("Enter a word here: ")
print (foo(x))
vowels = ["A", "E", "I", "O", "U"]
new = ["*", "*", "*","*", "*"]
for i in range(1):
    new_word = foo(x).replace(vowels[i],new[i])
print(new_word)
