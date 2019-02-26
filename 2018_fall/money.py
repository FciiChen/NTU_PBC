row_1 = input()
row_1 = row_1.split(",")
num = int(row_1[0])
price = int(row_1[1])
require = int(row_1[2])

row_2 = input().split(",")
row_3 = input().split(",")

pro = 0
best_pro = 0
best_trade = 0
min_fix_cost = 0

for i in range(num):
    pro = ( price - int(row_3[i]) ) * require - int(row_2[i])
    if (pro >= 0) and (pro >= best_pro):
        if (pro > best_pro):
            best_pro = pro
            best_trade = i+1
            min_fix_cost = row_2[i]
        elif (pro == best_pro) and (row_2[i] < min_fix_cost):
            best_pro = pro
            best_trade = i+1
            min_fix_cost = row_2[i]    


print(best_trade, best_pro)