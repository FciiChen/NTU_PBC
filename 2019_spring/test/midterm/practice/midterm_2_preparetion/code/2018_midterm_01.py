keyin = input()
data1 = []

while(keyin != "BREAK"):
    keyin = keyin.split(",")
    keyin = [item.strip() for item in keyin]
    data1.append(keyin)

    keyin = input()

keyin = input()
data2 = []

while(keyin != "BREAK"):
    keyin = keyin.split(",")
    keyin = [item.strip() for item in keyin]
    data2.append(keyin)

    keyin = input()


for information in data1:
    flag = 0
    for item in data2:
        if (information[0].lower() == item[0].lower()):
            information.append(item[1])
            flag = 1
    if flag == 0:
        information.append("NULL")

for item in data1:
    for index, subitem in enumerate(item):
        print("%-10s"%subitem, end = "")
        if(index != len(item)-1):
            print(" ", end = "")
    print()