def gen_random(problist, runif): #develop your function here.
    sum_of_prob = 0
    for probs in problist:
        sum_of_prob += probs

    if (abs(1-sum_of_prob) >= 10 ** -6) or (runif > 1) or (runif < 0) :
        return None

    interval, bottom  = 0, 0
    #print(runif)
    for probs in problist:
        upbound = bottom + probs
        upbound = int(upbound*10000000)/10000000
        #print (upbound)
        if abs(1 - upbound) <= 10 ** -6 :
            upbound = 1

        #print(bottom, upbound)
        if upbound >= runif > bottom:
            break
        elif upbound >= runif >= bottom and bottom == 0:
            break
            
        interval += 1   
        bottom += probs 
        #bottom = bottom + probs 
        #bottom = upbound
       # print(bottom)
        
         


    return interval


prob = input()
ru = float(input())
prob = prob.split(',')

for i in range(len(prob)):
    prob[i] = float(prob[i])

out1 = gen_random(prob, ru) 
if(out1 == None):
    print("DATA_ERROR")
else: 
    print(out1)