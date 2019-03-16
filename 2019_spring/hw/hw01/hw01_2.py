p1 = int(input())
p2 = int(input())

x1 = int(input())
x2 = int(input())
x3 = int(input())
summ = 0

summ += p1 * x1 + p2 * x2 

if (p1 >= p2): # if p1 >= p2, swap(p1,p2), which makes p1 always smaller than (or equal to ) p2
    temp = p1
    p1 = p2
    p2 = temp

summ += p1 * x3 # p1 is surely smaller, because the abovementioned code which swap a and b, so we choose p1 as the price

money = summ % 1000 #money is allowance

if (money > 500): 
    temp_money = money
    money = 500
    money += int( (temp_money - 500)/2 ) 

bonus = -1 # we make "bonus" defaultedly be -1, so that if we don't have bonus, it would surely be -1 

if (money % 100 == 0):
    bonus = money * 0.1
    money += bonus

print(int(bonus), int(money))