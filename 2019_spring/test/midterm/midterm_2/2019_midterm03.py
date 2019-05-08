from datetime import datetime

file = input()
file = open(file, 'r', encoding = "cp950")

line = file.readline() #to read the file
script = [] #a list which contains each line of file
while line:
    line = line.split("\t")
    line = [item.strip() for item in line]
    script.append(line) #append every line
    line = file.readline()

#print(script)
script = script[1:]

for data in script:
    data[2] = datetime.strptime(data[2], "%Y%m%d")

sortedlist = sorted(script, key=lambda kv: kv[2])

#print(sortedlist)

sorteddict_month = {}
for data in script:
    if not str(data[2].year)+ ", " +str(data[2].month) in sorteddict_month :
        sorteddict_month[str(data[2].year)+ ", " +str(data[2].month)] = [data]
    else:
        sorteddict_month[str(data[2].year)+ ", " +str(data[2].month)].append(data)
    
#print(sorteddict_month)


for k in sorteddict_month:
    maxvalue = 0
    minvalue = 10**5
    sum_value = 0
    for i in range(len(sorteddict_month[k])):
        if maxvalue < float(sorteddict_month[k][i][4]):
            maxvalue = float(sorteddict_month[k][i][4])
        if minvalue > float(sorteddict_month[k][i][5]):
            minvalue = float(sorteddict_month[k][i][5])
        sum_value += int(sorteddict_month[k][i][7])
    
    sorteddict_month[k] = [sorteddict_month[k][0][0], sorteddict_month[k][0][2],sorteddict_month[k][0][3], "%.2f"%maxvalue, "%.2f"%minvalue, sorteddict_month[k][-1][6], str(sum_value)]

for k in sorteddict_month:
    sorteddict_month[k][1] = sorteddict_month[k][1].strftime("%Y%m%d")
    ans_str = str()
    for information in sorteddict_month[k]:
        ans_str += information + ","
    print(ans_str[:-1])
