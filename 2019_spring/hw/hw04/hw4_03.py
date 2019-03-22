guest_and_master = input().split(",")
guest_and_master = [int(i) for i in guest_and_master]
guest = guest_and_master[0]
master = guest_and_master[1]

need_time = input().split(",")
need_time = [int(i) for i in need_time]

reserve_time = input().split(",")
reserve_time = [int(i) for i in reserve_time]

profit = input().split(",")
profit = [int(i) for i in profit]

number = [i for i in range(guest)]

def swap_things(i,j):
    need_time[i], need_time[j] = need_time[j], need_time[i]
    profit[i], profit[j] = profit[j], profit[i]
    reserve_time[i], reserve_time[j] = reserve_time[j], reserve_time[i]
    number[i], number[j] = number[j], number[i]

for i in range(guest): #need_time, profit, number
    for j in range(i+1, guest):
        if need_time[i] > need_time[j]:
            swap_things(i,j)
        elif need_time[i] == need_time[j] and reserve_time[i] > reserve_time[j]:
            swap_things(i,j)
        elif need_time[i] == need_time[j] and reserve_time[i] == reserve_time[j] and number[i] > number[j]:
            swap_things(i,j)
'''
print(need_time)
print(reserve_time)
print(number)
'''

num_had_service = 0 #the total amount of guest we've serviced
total_profit = 0
master_schedule = [ [0]*360 for i in range(master) ]
work_time_limit = 360 #the limit of the worktime of massage master 

for num in range(guest): 
    best_master_choice = 0 #to record the best master under the condition we want
    min_wait_time = 31 #the wait time limit is 30, yet I set it as 31 because the first time 30 is accpectable
    no_one_can_service = True
    
    for master_no in range(master): 
        if reserve_time[num] + need_time[num] > work_time_limit: #it's obviously can't work, cuz' the store is closed then
            break

        '''
        The following check_time_end is a important condition set: +1 to confirm the boundary value
        '''
        check_time_end = reserve_time[num]+30+1 if reserve_time[num]+30 < 360-need_time[num] else 360-need_time[num]+1

        for i in range(reserve_time[num], check_time_end): #from the time reserved to the waitime limit the guest can accept
            time_avail_status = True
            for j in range(i, i+need_time[num]): #to check if start at i whether the interval of time we go through is available
                if master_schedule[master_no][j] == 1:
                    time_avail_status = False
                    break
            
            if time_avail_status == True: #if we find a interval is available, record and break
                wait_time = i - reserve_time[num] #Time the guest need to wait
                no_one_can_service = False #there's at less a person can provide service
                start_time = i #the time that guest start to get the service
                break
        #print(wait_time)

        if wait_time == 0 and no_one_can_service == False : #if there's a master idle we pick him immediately
            best_master_choice = master_no
            min_wait_time =  wait_time
            best_start_time = start_time
            break
        elif wait_time < min_wait_time and no_one_can_service == False: #if a master can make guest wait shorter, we pick him
            min_wait_time =  wait_time
            best_start_time = start_time
            best_master_choice = master_no
    
    #print(best_master_choice)

    #print(best_start_time)
    if no_one_can_service == True:
        #print("!!!!\n")
        pass
    else:   
        for k in range(best_start_time, best_start_time+need_time[num]): #set that interval of time unavailable
            master_schedule[best_master_choice][k] = 1
        total_profit += profit[num] #add the profit the guest gives
        num_had_service += 1 #add 1 guest
        '''
        print(best_master_choice)
        print(master_schedule)
        print()
        '''            

print(str(num_had_service) + "," + str(total_profit)) #print out the ans