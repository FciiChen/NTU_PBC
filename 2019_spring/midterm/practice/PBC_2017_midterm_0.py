import math
num = int(input())

if (num % 7 == 0):
    print(1)
elif (num == int(math.sqrt(num)) **2 ):
    print(2)
else:
    print(3)