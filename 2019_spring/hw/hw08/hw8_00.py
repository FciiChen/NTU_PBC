keyin = input().split(",")

xk = int(keyin[0])
num_of_ran = int(keyin[1])

ans_str = str()

for i in range(num_of_ran):
    xk = str(pow(xk, 2))[-12:-4].lstrip("0") if str(pow(xk, 2))[-12:-4].lstrip("0") != "" else "0"#get the 5th ~ 12th digits of pow of xk 
    ans_str += xk + ","
    xk = int(xk) ##change back to num type
     
print(ans_str[:-1])