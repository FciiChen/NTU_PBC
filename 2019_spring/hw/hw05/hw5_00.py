def ewp(alpha, ylist):
    alpha = float(alpha)

    if (alpha < 0 or alpha > 1):
        return None
    if (len(ylist) < 5):
        return None

    summ = 0

    for y_item in ylist:
        #print(type(alpha))
        summ = summ * (1-alpha) + alpha * float(y_item)
    
    return summ
        
    
alpha = input()
ystr = input()
yall = ystr.split(',')

out1 = ewp(alpha, yall)
if(out1 == None):
    print("ERROR")
else:
    print("%0.6f" % out1)