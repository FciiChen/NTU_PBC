num = int(input())

ans_string = str()
for i in range(1, 1+num):
    if (i % 7 == 0) or (i % 10 == 7):
        ans_string += "*" + ","
    else:
        ans_string += str(i) + ","

print(ans_string[:-1])