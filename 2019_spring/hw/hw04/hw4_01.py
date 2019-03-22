num = int(input())

price = input().split(",")
price = [int(i) for i in price]

request = input().split(",")
request = [int(i) for i in request]

cost = input().split(",")
cost = [int(i) for i in cost]

profit = 0
for i in range(num):
    profit += (price[i] - cost[i]) * request[i]

print(profit)