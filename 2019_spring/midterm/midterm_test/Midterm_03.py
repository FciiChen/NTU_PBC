num = int(input())

array = []
for i in range(num):
    temp_array = input().split(",")
    temp_array = [int(i) for i in temp_array]
    array.append(temp_array) #i_row = 橫行(frst label) j_row = 直列(second label)

yes_pairs = []

for i in range(num):
    for j in range(num):
        if array[i][j] == array[j][i] and i < j:
            yes_pairs.append([i,j])

#print(yes_pairs)
#print(len(yes_pairs))

for i in range(len(yes_pairs)):
    for j in range(i+1, len(yes_pairs)):
        if yes_pairs[i][1] > yes_pairs[j][1]:
            yes_pairs[i], yes_pairs[j] = yes_pairs[j], yes_pairs[i]
        elif yes_pairs[i][1] == yes_pairs[j][1] and yes_pairs[i][0] > yes_pairs[j][0]:
            yes_pairs[i], yes_pairs[j] = yes_pairs[j], yes_pairs[i]

if len(yes_pairs) == 0:
    print(-1)
else:
    for i in yes_pairs:
        string = str()
        string += str(i[0]+1) + " " + str(i[1]+1)
        print(string)