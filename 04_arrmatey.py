import sys
i=0
for argv in sys.argv:
        print("Argv of "+str(i) + " is "+  str(sys.argv[i]))
        i=i+1
sys.argv.sort(key = len, reverse = True)
for x in sys.argv:
    print(x)
        
        
