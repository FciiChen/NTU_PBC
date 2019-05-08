
import sys

def dist(a1, a2): # weighted distance between a1, a2
    sum=0.0
    len1 = len(a1)
    len2 = len(a2)
    if len1 != len2:
        raise Exception("Error: length not the same")

    M = (len1 + 1)* len1 / 2.0
    for i in range(len1):
        sum += ((len1-i)/M)**2 * (a1[i] - a2[i])**2

    return sum**0.5


allinput=[]
while(1):
    tmp=input()
    if tmp=="BREAK":
        break
    else:
        allinput.append(tmp.strip())

if len(allinput) < 4:
    print("ERROR")
    sys.exit(-1)

ally = []
allx = []
for i in range(len(allinput)-2):
    aline = allinput[i]
    #print(aline)
    tmp1 = aline.split(',')
    try:
        ally.append(float(tmp1[0]))
        tmp2 = [float(x) for x in tmp1[1:]]
        allx.append(tmp2)
    except:
        print("ERROR")
        sys.exit(-1)

#deal with a, k
aline = allinput[-2]
tmp1 = aline.split(',')
try:
    a = [float(x) for x in tmp1]
    k = int(allinput[-1])
except:
    print("ERROR")
    sys.exit(-1)

if k <= 0:
    print("ERROR")
    sys.exit(-1)



#print("a = ", a)
#print("k = ", k)
alldist = []
for i in range(0, len(allx)):
    try:
        tmp2 = dist(a, allx[i])
    except:
        print("ERROR")
        sys.exit(-1)
    alldist.append(tmp2)
    #print("%0.5f" % tmp2)

#now, sort and do prediction.
#need to think about the case when distance tie.
#print(alldist)
sindex = sorted(range(len(alldist)), key=lambda k: alldist[k])

sum0 = 0.0
if k > len(allx):
    k = len(allx)
for i in range(k):
    sum0 += ally[sindex[i]]
ypred = sum0 / k
#print("Prediction = ", ypred)
print("%0.3f" %  ypred)