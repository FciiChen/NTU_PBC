import csv
fn1 = input()

fh1 = open(fn1, 'r', newline = '', encoding = 'utf-8') # open file

csv1 = csv.DictReader(fh1) # read csv
cname1 = csv1.fieldnames # header
data1 = dict()
for aline in csv1:
    #print(aline)
    key = aline[cname1[0]].strip()
    value = aline[cname1[1]].strip()
    if key not in data1:
        data1[key] = [value]
    else:
        data1[key].append(value)


#to merge data1 and data2
key1 = list(data1.keys())
key1.sort()

for akey in key1:
    print(akey + "," + ",".join(data1[akey]))
