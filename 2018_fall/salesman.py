import math
n = int(input())
p = float(input())

def factorial(n):
    ans = 1
    for i in range(n+1):
        if (i != 0):
            ans *= i
    return ans

n_ = factorial(n)
ans_list = []
for i in range(n+1):
    ans_list.append( pow(1-p, n-i) * pow(p, i) * n_ / (factorial(i) * factorial(n-i))  )

print(",".join( str(int(i*100)) for i in ans_list))

