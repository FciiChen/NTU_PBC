line = input()

sepchar = [" " , "," , "\\" , "\'" , "\"" , ";" , "." , "!" , ":" , "(" , ")" , "[" , "]" , "{" , "}" , "\n" , "\r" , "\t" , "=", "+" , "/"  , ">", "<"]

for i in sepchar:
    #print(line)
    line = line.replace(i," ")


line = line.split()

for i in range(len(line)):

    line[i] = line[i].strip().lower()
    print (line[i])