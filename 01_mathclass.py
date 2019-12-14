import math
import sys

i=0
the_number = []

for argv in sys.argv:
    the_number.append(sys.argv[i])
    i = i+1
del the_number[0]

for x in range(0,len(the_number)):
    the_number[x] = int(the_number[x])
Sum = sum(the_number)
print(the_number)

print("Mean: " ,Sum/len(the_number))

print("Min: " ,min(the_number))

print("Max: " ,max(the_number))

print("Range: " ,max(the_number)-min(the_number))
