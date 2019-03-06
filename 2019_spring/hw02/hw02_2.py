cost = int(input())
a1 = int(input())
r1 = int(input())
r2 = int(input())

a2 = a1 + r1
a3 = a2 - r2 
max_profit = best_q = best_price = 0 #set up these varible to record the profit, require, and price in the best price

price = cost #we know that price - cost should be >= 0

while (1):

    if (0 <= price < r1):
        require = a1 - price if (a1 - price > 0) else 0 #to make sure that require > 0

    elif (r1 <= price < r2):
        require = a2 - 2*price if (a2 - 2*price > 0) else 0 #to make sure that require > 0

    elif (r2 <= price < a3):
        require = a3 - price if (a3 - price > 0) else 0 #to make sure that require > 0

    else:
        require = 0

    profits = (price - cost) * require
    #print(profits, price, require)
    if (profits > max_profit) or (profits == max_profit and price == cost): 
        '''
        everytime when there's a better solution, renew value.
        Also, when we fisrt time run the loop, price == cost, so that profits == max_profitbut == 0, 
        but we should still renew the variable or we may get, 
        or if any price will get 0 profits, we'll get 0, 0, 0, which is wrong
        '''
        max_profit = profits
        best_price = price
        best_q = require

    if (require == 0) and (price != cost):
        break  
    
    price += 1
    

print(best_price, best_q, max_profit)
