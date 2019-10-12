list1=[False,True,True,None,True,None,None,False,False,None,True,False]
list2=["or","or","or","==","!=","==","and","==","!=","and","==","or"]
list3=[False,False,None,None,True,True,False,True,None,False,True,None]


for x in range(12):
    b = (str(list1[x]) + " " + list2[x] + " " + str(list3[x]))
    x=eval(b)
    print(b+" => " + str(x))
