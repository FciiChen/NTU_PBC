import math
num = int(input())

if (num % 7 == 0):
    print(1)
elif (num / math.sqrt(num) ==  math.sqrt(num)):
    print(2)
else:
    print(3)