num = int(input())

hundred = (num // 100)%10 
ten = (num // 10)%10

if num == ( hundred*10 + ten ) ** 2:
    print(hundred*10 + ten, 1)
else:
    print(hundred*10 + ten, 0)
