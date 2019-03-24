num = int(input())

f_array = [0, 1]

for i in range(2, num+1):
    new = f_array[i-1] + f_array[i-2]
    f_array.append(new)

print(f_array[num])