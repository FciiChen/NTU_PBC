num = int(input())

price = input().split(",")
price = [int(i) for i in price]

buy = input().split(",")
buy = [int(i) for i in buy]

cost = input().split(",")
cost = [int(i) for i in cost]

one_good_max_profit = 0
for i in range(num):
    profit = ( price[i] - cost[i] ) * buy[i]
    if profit > one_good_max_profit:
        one_good_max_profit = profit

mutiple_good_profit = 0
for i in range(num):
    profit = ( price[i] - cost[i] ) * buy[i]
    if profit >= 0 :
        mutiple_good_profit += profit

print(one_good_max_profit, mutiple_good_profit)