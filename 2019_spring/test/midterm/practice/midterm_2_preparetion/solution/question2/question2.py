
import sys

allinput1=[]
allinput2=[]
count = 0 # 0 for input1 , 1 for input2
while(1):
    tmp=input()
    if tmp=="BREAK":
        if count == 0:
            count += 1
            continue
        else:
            break
    else:
        if count == 0:
            allinput1.append(tmp.strip())
        else:
            allinput2.append(tmp.strip())

#print("allinput1=", allinput1)
#print("allinput2=", allinput2)

recmap = dict() # turn input2 into dictionary
for arec in allinput2:
    tmp1 = arec.split(',')
    recmap[tmp1[0].strip().lower()] = tmp1[1].strip()

#print(recmap)
#output
for arec in allinput1:
    tmp1 = arec.split(',')
    tmp1 = [x.strip() for x in tmp1]
    if tmp1[0].lower() in recmap:
        tmp1.append(recmap[tmp1[0].lower()])
    else:
        tmp1.append("NULL")
    tmp2 = ['%-10s' % x for x in tmp1]
    print(" ".join(tmp2))


