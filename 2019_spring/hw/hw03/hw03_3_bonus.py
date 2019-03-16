row_1 = input() #the row 1 of input
row_2 = input() #the row 2 of input
row_3 = input() #the row 3 of input

row_1 = row_1.split(",") #make row_1 a list by seperating the variables by ","

guest_and_massage_master = [] #a temp list to write in guest and massage master
for item in row_1: #use for loop to int() things contain in list row_1, and append it toanother list
    guest_and_massage_master.append(int(item))

guest = guest_and_massage_master[0] #guest's number
massage_master = guest_and_massage_master[1] #master's number

''''''

row_2 = row_2.split(",") #make row_2 a list by seperating the variables by ","
time = [] 
for item in row_2: #use as the abovementioned usage in row 7
    time.append(int(item))

''''''

row_3 = row_3.split(",") #make row_3 a list by seperating the variables by ","
profit = [] #profit we'll get when we finish certain guest, which we use list to record
for item in row_3: #use as the abovementioned usage in row 7
    profit.append(int(item))

worktime_of_master = [0] * massage_master #a list to record the total time massage masters work
total_profit = 0 #to sum up the profit
num_had_service = 0 #the total amount of guest we've serviced

for i in range(guest): #time, profit, number
    for j in range(i+1, guest):
        if time[i] > time[j]:
            time[i], time[j] = time[j], time[i]
            profit[i], profit[j] = profit[j], profit[i]
        elif time[i] == time[j] and profit[i] < profit[j] :
            time[i], time[j] = time[j], time[i]
            profit[i], profit[j] = profit[j], profit[i]
            

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