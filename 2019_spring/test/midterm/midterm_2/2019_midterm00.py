from datetime import datetime
import sys

line = input()
data = []
raw_data = []

while(line != "BREAK"):
    raw_data.append(line)
    line = input()

for row in raw_data:
    try:
        datetime_obj = datetime.strptime(row, "%Y/%m/%d")
    except:
        print("DATA_ERROR")
        sys.exit()
    data.append(datetime_obj)

#print(data)

weekday_count = ([1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0])
for item in data:
    weekdaynum = item.weekday()
    for i in weekday_count:
        if weekdaynum+1 == i[0]:
            i[1] += 1

#print(weekday_count)


for i in weekday_count:
    print(i[0], i[1])