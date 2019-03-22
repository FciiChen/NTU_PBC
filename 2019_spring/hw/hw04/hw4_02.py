town_and_hospital = input().split(",") #row 1 are num of town and hospital
for i in range(2):
    town_and_hospital[i] = int(town_and_hospital[i]) #chage the datatype

town = town_and_hospital[0]
hospital_amount = town_and_hospital[1]

relationship = [] #the relationship between cities. if there's one road, we set the relationship = 1, otherwise = 0
for i in range(town): #i is for row and j is for column
    row = input().split(",")
    for j in range(town):
        row[j] = int(row[j])

    relationship.append(row) #the result would be a two dimension list

hospital_num = input().split(",") #the number of the city which will set up hosptial
for i in range(hospital_amount):
    hospital_num[i] = int(hospital_num[i]) - 1 

set_status = [0]*town #the list to record wether or not the city can approach the hospital, if it can value = 1, otherwise = 0

for i in hospital_num: #we check rows given by the Question, which are the cities set up the hospital
    for j in range(town): #check the relationship between other cities and the now chosen city
        if (relationship[i][j] == 1) or (i == j): #if there's a road or it's just the city set the hospital, set value = 1
            set_status[i] = 1
            set_status[j] = 1

#print(set_status)

ans_status = True #we assume that every city could approach the hospital using the method we set the hospital by
not_set = str() #we set a string to record the city that can't approach the hospital

for i in range(town):
    if (set_status[i] == 0 ):
        ans_status = False #if there's no road , we set ans_status = 0, which means the method we set the hospital by can't contian every city
        not_set += str(i+1) + ","

if ans_status == False:
    print(not_set[:-1]) #don't print the last ","
else:
    print(-1) #if the method works, print(-1)