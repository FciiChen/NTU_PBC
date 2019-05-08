array = input().split(" ")

array = [int(i) for i in array]
y_and_z = input().split(" ")
y_and_z = [int(i) for i in y_and_z]

for i in array:
    if i == y_and_z[0]:
        array.remove(i)


string = str()
if y_and_z[1] == 0:

    for i in array:
        string += str(i) + " "
    
    print(string[:-1])
else:
    for i in range(len(array)-1, -1, -1):
        string += str(array[i]) + " "

    print(string[:-1])