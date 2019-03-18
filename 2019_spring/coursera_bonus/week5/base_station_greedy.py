temp = input().split()
temp = [int(i) for i in temp]

town, pick, range_dis = temp[0], temp[1], temp[2] #num of town, num of base station , radiation range
x, y = [], [] #x, y coordinate
population = []
dis = [] #distance
unchoose_town = [i for i in range(town)] #the city not yet choose

for i in range(town):
    temp = input().split()
    temp = [int(i) for i in temp]
    x.append(temp[0])
    y.append(temp[1])
    population.append(temp[2])
#print(unchoose_town)

for i in range(town):
    dis.append([]) #to set up a two demension list
    for j in range(town):
        x_diff = x[i] - x[j]
        y_diff = y[i] - y[j]
        dis[i].append( pow(x_diff**2 + y_diff**2, 1/2) )

ans = str()
total_population = 0

while(pick > 0): 
    
    best_population = 0
    for i in unchoose_town:
        temp_population = population[i]
        for j in unchoose_town:
            if dis[i][j] <= range_dis and j != i: #because we'd set temp_population = population[i], we shouldn't count itself again
                temp_population += population[j]

        if best_population < temp_population:     
            best_population = temp_population
            best_point = i

    #print(best_point)
    
    total_population += best_population
    ans += str(best_point + 1) + " "

    for i in unchoose_town: #the point chosen should be 0 population, or we'll count again
        if dis[best_point][i] <= range_dis:
            population[i] = 0
    
    unchoose_town.remove(best_point) #remove the point chosen
    pick -= 1 #every time we pick one point, minus 1

ans += str(total_population)
print(ans)
