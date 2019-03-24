row_1 = input().split(",")
row_1 = [int(i) for i in row_1]
num = row_1[0]
a_constant = row_1[1]
b_constant = row_1[2]
cost = row_1[3]

row_2 = input().split(",")
row_2 = [int(i) for i in row_2]
row_2.sort()

best_buy_in_price = 0
best_profit = 0


for buy_in_price in row_2:
    test_best_price = 0
    test_best_profit = 0
    for price in range(buy_in_price+1, a_constant//b_constant+1):
        test_profit = (price - buy_in_price) * (a_constant - b_constant*price)
        if test_profit > test_best_profit:
            test_best_profit = test_profit
            test_best_price = price

    profit = (buy_in_price - cost) * (a_constant - b_constant*test_best_price)
    if profit > best_profit:
        best_profit = profit
        best_buy_in_price = buy_in_price
        best_price = test_best_price

print(best_buy_in_price, best_price, a_constant - b_constant*best_price, best_profit)

