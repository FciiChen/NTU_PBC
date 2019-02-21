num_and_weight = input()
num_and_weight = num_and_weight.split()
#print (num_and_weight)
max_weight = int(num_and_weight[1])
max_num = int(num_and_weight[0])

weight = input()
weight = weight.split()
use = input()
use = use.split()



checkcase = input()
checkcase = int(checkcase)

#print(checkcase)


backpack = []

for case in range(checkcase):
    temp = input()
    backpack.append(temp.split())

best_case = 0
best_use = 0
best_weight = 0
best_chosen = max_num
best_min_chosen = max_num+1

for case in backpack:
    #print(case)

    now_use = 0
    now_weight = 0
    pos = 0
    chosen = 0
    min_chosen = 0
    status = False
    
    for i in range(1, max_num+1):
        now_use += int(case[i]) * int(use[pos]) 
        now_weight += int(case[i]) * int(weight[pos])
        '''print(int(case[i]))
        print(use[pos])
        print(weight[pos])
        print(now_use)
        print(now_weight,"\n")'''
        pos += 1
        chosen += int(case[i])
        if (int(case[i]) == 1) and (min_chosen == 0):
            min_chosen = i
            #print(min_chosen)
        

    if (now_use >= best_use ) and (now_weight <= max_weight):
        if (now_use > best_use ):
            status = True
        elif (now_use == best_use) and (chosen <= best_chosen):
            if (chosen > best_chosen):
                status = True
            elif (chosen == best_chosen) and (min_chosen < best_min_chosen):
                status = True
                
                
    if status == True:
        best_min_chosen = min_chosen
        best_case = case[0]
        best_use = now_use
        best_weight = now_weight
        best_chosen = chosen
        best_min_chosen = min_chosen


print (best_case, best_weight, best_use )


'''
#print(num)
#print(weight)
'''