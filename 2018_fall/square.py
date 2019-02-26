x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

lenght = x1 - x2
width = y1 - y2
if ( lenght == width ):
    print(1, lenght * width)
else:
    print(0, lenght * width)

