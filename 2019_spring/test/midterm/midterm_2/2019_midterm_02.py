pun = "0123456789(),$"

file = input()
file = open(file, 'r', encoding = 'utf-8')

line = file.readline() #to read the file
script = [] #a list which contains each line of file
while line:
    script.append(line.rstrip()) #append every line
    line = file.readline()

#print(script)

### find all 跳連詞
grade_record = {}
for index, setence in enumerate(script):
    grade = 0
    for subindex, letter in enumerate(setence):
        for i in pun :
            if i == setence[subindex]:
                grade += 1
        grade_record[index] = grade

new_grade_record = {}
for k,v in grade_record.items():
    if not v in new_grade_record:
        new_grade_record[v] = [k]
    else:
        new_grade_record[v].append(k)

sortedlist = sorted(new_grade_record.items(), key=lambda kv: kv[0], reverse = True)

for item in sortedlist:
    item[1].sort()

#print(sortedlist)

### output

count = 0
for item in sortedlist:
    if count == 10:
        break
    for subitem in item[1]:
        print("@%d: "%(subitem+1) + script[subitem])
        count += 1
        if count == 10:
            break