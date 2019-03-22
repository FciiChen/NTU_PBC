x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

max_y = y1
max_part = 1

if y2 > max_y:
    max_y = y2
    max_part = 2
    
if y3 > max_y:
    max_y = y3
    max_part = 3


slope_1 = (y2-y1) / (x2-x1)
slope_2 = (y3-y2) / (x3-x2)


if slope_1 == slope_2:
    print(1, max_part)
else:
    print(0, max_part)