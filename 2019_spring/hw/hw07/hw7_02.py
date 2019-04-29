file = input()
file = open(file, 'r', encoding = 'utf-8')
keyword_to_process = input()

def data_processing(to_process): #to lower, replace the tab by space, take off the unneeded space, and strip the string
    to_process = to_process.lower()

    to_process = to_process.replace("\t", " ") #replace tab by space

    to_process = to_process.split(" ") #take off surplus space: from here ->
    data_processed = str()
    for letter in to_process:
        if letter != "":
            data_processed += letter + " "
    data_processed = data_processed.strip()
    return data_processed #to here <-

key_word = data_processing(keyword_to_process) #make key word be the form asked by the question
#print(key_word)

line = file.readline() #to read the file
script = [] #a list which contains each line of file
while line:
    script.append(line) #append every line
    line = file.readline()

num_of_match = 0 #to record how many line we've matched

for index in range(len(script)): #go through the list
    
    if key_word in data_processing(script[index]): #if the key word is in the processed line

        num_of_match += 1 #then num +1
        if index == 0: #if that line if the first line
            nowline = script[index]
            nextline = script[index+1]
            print("----Match", num_of_match)
            print("    @%d: " %(index)) 
            print("    @%d:" %(index+1), nowline.strip())
            print("    @%d:" %(index+1+1), nextline.strip())
            
        elif index == len(script)-1: #if that line if the last line
            lastline = script[index-1]
            nowline = script[index]
            print("----Match", num_of_match)
            print("    @%d:" %(index-1+1), lastline.strip())
            print("    @%d:" %(index+1), nowline.strip())
            print("    @%d: " %(index+1+1))
            
        else: #other lines
            lastline = script[index-1]
            nowline = script[index]
            nextline = script[index+1]
            print("----Match", num_of_match)
            print("    @%d:" %(index-1+1), lastline.strip()) 
            print("    @%d:" %(index+1), nowline.strip())
            print("    @%d:" %(index+1+1), nextline.strip())
