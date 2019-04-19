line = input()
line.strip()

line.replace("\t"," ")

line = line.split()

for i in range(len(line)):
    line[i] = line[i].strip()

ans_str = str()
for item in line:
    ans_str += item + " "

print (ans_str[:-1])
