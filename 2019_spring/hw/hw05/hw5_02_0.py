import math

def logic(alist, clist):
    return 1 / (1 + math.exp( -(clist[0] + clist[1]*alist[0] + clist[2]*alist[1]) ))


alist = input().split(",")
clist = input().split(",")

alist = [int(i) for i in alist]
clist = [float(i) for i in clist]

print("%0.6f" %(logic(alist, clist)))