import math

row_1 = input().split(",")
row_1 = [int(i) for i in row_1]

yes_pairs = 0
for i in range(len(row_1)):
    for j in range(i+1, len(row_1)):
        now_sum = row_1[i] + row_1[j]
        #print(now_sum)
        if now_sum == int(math.sqrt(now_sum)) ** 2:
            yes_pairs += 1

print(yes_pairs)