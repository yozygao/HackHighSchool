import random
clist=['Overwatch ' ,'BTS ',]
alist=[]
x=random.choice(clist)
print("Your category is " + x)
answers= []

if x=="Overwatch ":
    for i in range(10):
        answers.append(input(" "))

if x=="BTS ":
    for i in range(10):
        answers.append(input(" "))
a = ("Your answers are " + str(answers))
print(a.center(100))
