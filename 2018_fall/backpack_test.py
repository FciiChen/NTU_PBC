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


now_use = 0
now_weight = 0

best_case = 0
best_use = 0
best_weight = 0

for case in backpack:
    #print(case)
    pos = 0

    for i in range(1, max_num+1):
        now_use += int(case[i]) * int(use[pos]) 
        now_weight += int(case[i]) * int(weight[pos])
        '''print(int(case[i]))
        print(use[pos])
        print(weight[pos])
        print(now_use)
        print(now_weight,"\n")'''
        pos += 1
        

    if (now_use > best_use ) and (now_weight <= max_weight):
        best_case = case[0]
        best_use = now_use
        best_weight = now_weight
        now_use = 0
        now_weight = 0
        #print("1!")

    else:
        now_use = 0
        now_weight = 0
        #print("2!")
        pass

print (best_case, best_weight, best_use )


'''
#print(num)
#print(weight)
'''