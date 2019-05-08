import csv
fn1 = input()
fh1 = open(fn1, 'r', newline = '', encoding = 'utf-8')
csv1 = csv.DictReader(fh1)
cname1 = csv1.fieldnames

ans_dict = {}


for aline in csv1:
    #print(aline)
 
    idname = aline[cname1[0]].strip()
    value = aline[cname1[1]].strip()
    
    
    if not (idname in ans_dict):
        ans_dict[idname] = value
    else:
        
        ans_dict[idname] = ans_dict[idname] + "," + value

key_list = list(ans_dict)
key_list.sort()

for key in key_list:
    print(key + "," + ans_dict[key])

#print(ans_dict)
