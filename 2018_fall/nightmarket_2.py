x = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())
y = int(input())

buy1, buy2, buy3 = 0, 0, 0

if (x - p1 >= 0):
    x -= p1
    buy1 = 1

if (x - p2 >= 0):
    x -= p2
    buy2 = 1

if (x - y*p3 >= 0):
    x -= y*p3
    buy3 = y

else:
    remain_money = x%p3
    buy3 = x//p3

print (str(buy1)+","+str(buy2)+","+str(buy3))
