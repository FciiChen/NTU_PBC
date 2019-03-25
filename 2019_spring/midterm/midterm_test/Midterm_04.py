row_1 = input().split(",")
row_1 = [int(i) for i in row_1]
num_of_city = row_1[0]
num_of_path_to_calculate = row_1[1]

relationship = []
for i in range(num_of_city):
    i_array = input().split(",")
    i_array = [int(k) for k in i_array]
    relationship.append(i_array)



path_to_calculate = []
for i in range(num_of_path_to_calculate):
    row_2 = input().split(",")
    row_2 = [int(i) for i in row_2]
    path_to_calculate.append(row_2)

#print(relationship)
#print(path_to_calculate)

ans_string = str()
for path in path_to_calculate:
    path_length = 0
    #print(path)
    for i in range(len(path)-1):
        if relationship[ path[i]-1 ][ path[i+1]-1 ] != -1:
            path_length += relationship[ path[i]-1 ][ path[i+1]-1 ] 
        else:
            path_length = -1
            break
    ans_string += str(path_length) + ","

print(ans_string[:-1])
