import math
import sys
from collections import Counter
i=0
the_number = []

for argv in sys.argv:
    the_number.append(sys.argv[i])
    i = i+1
del the_number[0]

for x in range(0,len(the_number)):
    the_number[x] = int(the_number[x])
Sum = sum(the_number)

print("Mean:" ,Sum/len(the_number))

print("Min:" ,min(the_number))

print("Max:" ,max(the_number))

print("Range:" ,max(the_number)-min(the_number))

the_number.sort()
n = len(the_number)

if n % 2 == 0:
    m1 = the_number[n//2]
    m2 = the_number[n//2-1]
    m = (m1 + m2)/2
else:
    m = the_number[n//2]
print("Median:" ,str(m))

data = Counter(the_number)
get_mode = dict(data)
mode =[k for k, v in get_mode.items() if v==max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode ="Mode:" + ', '.join(map(str,mode))
print(get_mode)

