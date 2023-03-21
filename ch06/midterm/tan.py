import math

x1 = 10
y1 = 10
xlist = [5, 15]
ylist = [5, 15]

for x in xlist: 
    for y in ylist:
        a = math.degrees(math.atan((y - y1)/(x - x1)))
        print(a)