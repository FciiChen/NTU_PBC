capital = int(input())
cost1 = int(input())
cost2 = int(input())
cost3 = int(input())
cost4 = int(input())
revenue = int(input())

status = 1 #use to break the while
while(status == 1):
    for day in range(1,8):
        
        if (day == 2) or (day == 5):
            capital -= cost3
        elif (day == 3):
            capital -= cost4
        elif (day == 7):
            capital += revenue
        
        if (day != 6) and (day != 7):
            capital -= cost1 +cost2
            print(str(capital) + ".", end = "") #no matter the number we print first

        if capital <= 0 : #however if this time the capital is already < 0, we break the while
            status = 0
            break
    

        
    
    

