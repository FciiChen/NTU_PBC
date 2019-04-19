line = input()
line += "," #for the folloing spilt rule 

quote = "\"" #make the following decision easier
comma = "," #make the following decision easier

ans_list = []

vaild_interval_start = 0 #end would be len(line) 
last_end = len(line) + 1 #the pos of last end-qoute 
last_comma = -1 #the pos of last comma

for index, word in enumerate(line): 
    
    if index != last_end and word == quote: #if this letter is a quote and it's not the second one of the pair of quote
        for i in range(index+1, len(line)): #to seek the other qoute of the pair
            if line[i] == quote: # if find
                last_end = i #set the last qoute pos to be i
                vaild_interval_start = i+1 #set the vaid interval of the method of spliting by comma
                break
    
    elif word == comma and index >= vaild_interval_start: #if the method of spliting by comma can be use in this interval and the letter is comma
        temp_str = str()

        for i in range(last_comma+1, index): #we make a string contains the letters from last_comma+1 to the letter followed by now letter
            temp_str += line[i]

        last_comma = index #renew the pos of the last last comma
        ans_list.append(temp_str)

#print(ans_list)

for item in ans_list: #output part
    print(item)
