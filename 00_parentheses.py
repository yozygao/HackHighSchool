print("eVeRy OtHeR lEtTeR cApItAlIzEd")
x = input("Enter a word: "
def removeVowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for c in word:
        if c.lower() in vowels:
            word = word.replace(c,"")
    return word
