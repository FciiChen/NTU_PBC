job = int(input())

duetime = input().split(",")
duetime = [int(i) for i in duetime]

worktime = input().split(",")
worktime = [int(i) for i in worktime]

number = [i for i in range(job)]

for i in range(job):
    for j in range(i+1, job):
        if duetime[i] > duetime[j]:
            duetime[i],duetime[j] = duetime[j],duetime[i]
            worktime[i],worktime[j] = worktime[j],worktime[i]
            number[i],number[j] = number[j],number[i]

        elif duetime[i] == duetime[j] and worktime[i] > worktime[j]:
            worktime[i],worktime[j] = worktime[j],worktime[i]
            number[i],number[j] = number[j],number[i]
        
        elif duetime[i] == duetime[j] and worktime[i] == worktime[j] and number[i] > number[j]:
            number[i],number[j] = number[j],number[i]

delaywork = 0
nowtime = 0 
for i in range(job):
    nowtime += worktime[i] 
    if (nowtime > duetime[i]):
        delaywork += 1


ans_string = str()
for i in range(job):
    ans_string += str(number[i] + 1) + " "
print(ans_string[:-1], end = ";")
print(delaywork)

