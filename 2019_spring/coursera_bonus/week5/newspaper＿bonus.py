cost = int(input()) 
price_per_goods = int(input())
request = int(input()) #需求的上限個數
remain = int(input()) #剩下的能賣多少單價

possible = []
for i in range(request+1):
    possible.append(float(input()))

maxprofit = 0
best_require = 0


for buy in range(request+1):
    profit = 0
    remain_possi = 1
    for sell in range(buy): #針對不同的買入量，去加總每種賣出量可能，到倒數第二種賣出可能
        profit += (sell*price_per_goods + remain*(buy-sell))*possible[sell]
        remain_possi -= possible[sell]
    profit += (buy*price_per_goods)*remain_possi #最後一種賣出可能，全賣，機率為剩下的所有機率加總
    profit -= buy*cost #扣掉成本
    
    if profit > maxprofit:
        maxprofit = profit
        best_require = buy

print (int(best_require), int(maxprofit))
