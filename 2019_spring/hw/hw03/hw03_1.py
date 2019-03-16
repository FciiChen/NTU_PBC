row_1 = input()
row_2 = input()

list_of_row_1 = row_1.split(",")
capital = int(list_of_row_1[0])
water = int(list_of_row_1[1])
salery = int(list_of_row_1[2])
food_cost = int(list_of_row_1[3])
bonus_cost = int(list_of_row_1[4])
life_length = int(list_of_row_1[5])

list_of_row_2 = row_2.split(",")
list_of_row_2 = [int(i) for i in list_of_row_2] #the revenue of every week
week = 1

for bonus in list_of_row_2:
    
    for day in range(1,8):
        
        if (day == 2) or (day == 5):
            capital -= food_cost
            capital -= water + salery
            if capital<=0 :
                break
        elif (day == 3):
            capital -= bonus_cost
            capital -= water + salery
            if capital<=0 :
                break
        elif (day == 6):
            pass
        elif (day == 7):
            capital += bonus
        else:
            capital -= water + salery
            if capital<=0 :
                break
        
    if capital <= 0: #shut down beforearrive the goal week 
        print(str(week-1)+','+str(capital))
        exit()
    elif week == life_length: #arrive the goal week
        print(str(life_length)+','+str(capital))
        exit()

    week += 1 #after one whole week week+1