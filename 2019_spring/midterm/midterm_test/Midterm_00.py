row_1 = input().split(",")
row_1 = [int(i) for i in row_1]

if len(row_1) == 1:
    print(row_1[0] ** 2)
elif len(row_1) % 2 == 0:
    print(row_1[ len(row_1)//2 - 1 ])
elif len(row_1) % 2 == 1:
    print(0)
    