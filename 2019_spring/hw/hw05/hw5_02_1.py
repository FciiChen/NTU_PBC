import math

def logic_margin(alist, clist, width):
    
    x1_p1 = 1 / (1 + math.exp( -(clist[0] + clist[1]*(alist[0]-width/2) + clist[2]*alist[1]) ))
    x1_p2 = 1 / (1 + math.exp( -(clist[0] + clist[1]*(alist[0]+width/2) + clist[2]*alist[1]) ))

    x2_p1 = 1 / (1 + math.exp( -(clist[0] + clist[1]*alist[0] + clist[2]*(alist[1]-width/2) )))
    x2_p2 = 1 / (1 + math.exp( -(clist[0] + clist[1]*alist[0] + clist[2]*(alist[1]+width/2) )))

    return (x1_p2 - x1_p1)/width, (x2_p2 - x2_p1)/width


alist = input().split(",")
clist = input().split(",")
width = float(input())

alist = [int(i) for i in alist]
clist = [float(i) for i in clist]

x1_margin, x2_margin = logic_margin(alist, clist, width)
print("%0.6f" %x1_margin)
print("%0.6f" %x2_margin)
