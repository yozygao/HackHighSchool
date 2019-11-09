import sys
import random

words = ["jimin" , "muzzy" , "hubba"]
x = random.choice(words)

lives = 0

print("The first letter of the word is" + " " + x[0])

while lives<10:
    y =  input("GUESS: ")
    if x == y:
        sys.exit("Good Job! You are one with the souce")
    if len(y) == 5:
        if x[0] !=  y[0]:
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ Now you know your ABC's. Please type a five letter word that starts with " + x[0] +"!")
    if len(y) != 5 and len(y) != 0:
        print("0, 1, 2, 3, 4 that’s how we count to five!")
    if len(y) == 0:
        print("You wasted a guess =P")
        lives = lives + 1
    if len(y) == 5:
        if x[0] == y[0]:
            lives = lives +1
            print("You have " +str(10-lives) + " lives left")
    else:
        if lives == 10:
            sys.exit("You lose :(")
