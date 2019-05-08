

pun = "　！？﹖。｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
pun += ' \n\t!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'  # punctuation

jump_dict = {}

article = input()
while(article != "BREAK"):

    for index in range(len(article)-2):
        flag = 0
        for item in pun:
            if item == article[index] or item == article[index+1] or item == article[index+2]:
                flag = 1
                break
        if flag == 1:
            continue
        else:
            jump_word = article[index] + "_" + article[index+2]
            if not jump_word in jump_dict:
                jump_dict[jump_word] = 1
            else:
                jump_dict[jump_word] = jump_dict[jump_word]+1

    article = input()

new_jump_dict = {}
for k,v in jump_dict.items():
    if not v in new_jump_dict:
        new_jump_dict[v] = [k]
    else:
        new_jump_dict[v].append(k)

'''
for i in jump_dict:
    print(i,jump_dict[i])
'''
sortedlist = sorted(new_jump_dict.items(), key = lambda kv:(kv[0]), reverse = True)

#print(sortedlist)

#for i in range(10):
#    print(sortedlist[i][0], sortedlist[i][1])

for item in sortedlist:
    item[1].sort()

#print(sortedlist)

count = 0
for item in sortedlist:
    if count == 10:
        break
    for subitem in item[1]:
        print(subitem, item[0])
        count += 1
        if count == 10:
            break
