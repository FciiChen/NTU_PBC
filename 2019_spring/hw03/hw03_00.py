row_1 = input()
row_2 = input()
row_3 = input()

num_and_cost = row_1.split(",")
num_of_case = int(num_and_cost[0])
cost_of_goods = int(num_and_cost[1])
list_of_price = row_2.split(",")
for i in range( len(list_of_price) ):
    list_of_price[i] = int(list_of_price[i])

list_of_require = row_3.split(",")
for i in range( len(list_of_require) ):
    list_of_require[i] = int(list_of_require[i])

best_profits = 0
best_require = 0
best_price = 0

for i in range( len(list_of_price) ):
    now_profit = ( list_of_price[i] - cost_of_goods ) * list_of_require[i]
    if now_profit > best_profits or (now_profit == best_profits and list_of_require[i] > best_require):
        best_profits = now_profit
        best_require = list_of_require[i]
        best_price = list_of_price[i]

print(str(best_price) + ',' + str(best_profits))