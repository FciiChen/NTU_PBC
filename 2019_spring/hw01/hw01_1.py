p1 = int(input())
p2 = int(input())

x1 = int(input())
x2 = int(input())
x3 = int(input())
summ = 0

summ += p1 * x1 + p2 * x2 

if (p1 >= p2): #if p1 >= p2, swap(p1,p2), which makes p1 always smaller than (or equal to ) p2
    temp = p1
    p1 = p2
    p2 = temp

summ += p1 * x3

print (summ % 1000)