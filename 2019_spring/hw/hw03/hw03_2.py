guest_and_massage_master = input() #the row 1 of input
time = input() #the row 2 of input
profit = input() #the row 3 of input

guest_and_massage_master = guest_and_massage_master.split(",") #make row_1 a list by seperating the variables by ","
for item in range(len(guest_and_massage_master)): #use for loop to int() things contain in guest_and_massage_master
    guest_and_massage_master[item] = int(guest_and_massage_master[item])

guest = guest_and_massage_master[0] #guest's number
massage_master = guest_and_massage_master[1] #master's number

''''''

time = time.split(",") #make row_2 a list by seperating the variables by ","
for item in range(len(time)): #use as the abovementioned usage in row 6
    time[item] = int(time[item])

''''''

profit = profit.split(",") #make row_3 a list by seperating the variables by ","
for item in range(len(profit)): #use as the abovementioned usage in row 6
    profit[item] = int(profit[item])

''''''

worktime_of_master = [0] * massage_master #a list to record the total time massage masters work
total_profit = 0 #to sum up the profit
num_had_service = 0 #the total amount of guest we've serviced


for num in range(0, guest): #go through every guest by their number
    min_time = 360 #the limit of the worktime of massage master 
    best_master_choice = 0 #to record the best master under the condition we want
    master_counter = 0 #to count the master's number which we are now checking
    for worktime in worktime_of_master: #go through master's worktime
        if (worktime < min_time) and (worktime + time[num] <= 360): #if fit the condition, it means it may be a good candidate
            min_time = worktime 
            best_master_choice = master_counter
        master_counter += 1 #to renew the number of master

    if (min_time == 360): #if min_time still equal to 360, means there's no master could service this guest, so sad.
        pass 
    else: #if there's one best master to do the service
        worktime_of_master[best_master_choice] += time[num] #plus time to his/her worktime
        total_profit += profit[num] #add the profit the guest gives
        num_had_service += 1 #add 1 guest

print(str(num_had_service) + "," + str(total_profit)) #print out the ans