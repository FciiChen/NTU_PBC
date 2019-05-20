class Event(): # a class to record event
    def __init__(self, name, t1, t2, eventval): #constructor
        self.name = name
        self.start = t1
        self.end = t2
        self.eventval = eventval #the value of the event

class Schedule():
    def __init__(self):#constructor
        self.now_event = [] #which means we automatically form a list when call this class

    def add_event(self, e): #to add the event into schedule
        self.now_event.append(e)
    
    def remove_event(self,e): ##to remove the event from schedule
        self.now_event.remove(e)

    def can_arrange(self, newevent): #to see whether we can put the now-judging event into the schedule
        status = True #we assume it can be arrrange by default
        for event in self.now_event: #to see through the schedule list
            if interval_conflict(event, newevent):
                status = False #we set it can't be arrange
                break
        #print(status)
        return status
    
    def show_total_value(self): #a func to show the total value of the schedule
        sum_value = 0 
        for event in self.now_event: #see through the schedule list
            sum_value += int(event.eventval) #we add the value of every event 
        return sum_value #and return the value
    
    def deletionwho(self, newevent): #a func to determine which to delete
        conflict_events = Schedule() 
        for event in self.now_event: #to see through the schedule list
            if interval_conflict(event, newevent):
                conflict_events.add_event(event) #put the now-existed event which conflict to the new event into the conflict_events
                
        if conflict_events.show_total_value() < int(newevent.eventval): #if the value of the new event is higher
            for event in conflict_events.now_event: #we remove all the now-existed event which conflict to the new event
                self.remove_event(event)
            self.add_event(newevent) #then append the new one
        else:
            pass
                

def interval_conflict(event, newevent): #a global func to see whether the interval is now occuped
    if change_to_sec(event.start) < change_to_sec(newevent.end) <= change_to_sec(event.end) or \
change_to_sec(event.start) <= change_to_sec(newevent.start) < change_to_sec(event.end) or \
( change_to_sec(event.start) >= change_to_sec(newevent.start) and change_to_sec(newevent.end) >= change_to_sec(event.end) ) :
        #if the start time or the end time of now-arranging event is within the interval of any now-existed event or it's totally contain the now-existed events
        #the "\" here is to avoid the code being too long
        return True #we return true
    else:
        return False 

def change_to_sec(event): #a global func to change the time's form from XX:XX:XX to seconds
    time_str = event.split(":")
    time_str = [int(i) for i in time_str]
    return time_str[0] * 3600 + time_str[1] *60 + time_str[2] #time_str[0] for hours, time_str[1] for minutes, and time_str[2] for seconds

def find_word(search_str, schedule): #to find the word which we want
    status = 0 #to see whether we find at least one event
    found_str = [] #put the event expected into the list
    for event in schedule.now_event:
        if search_str.lower() in event.name.lower():
            found_str.append(event)
            status = 1

    if status: #if we have find at least one event desired
        found_str.sort(key = lambda event: event.start) #sort by start time
        for event in found_str:
            print(event.name + "," + event.start + "," + event.end + "," + event.eventval)
    else: #if not find
        print("Nothing found.", end = "")

#============================== the following is the main part of the program ==============================


num_of_event = int(input()) #to determine how much event to arrange

calender = Schedule() 

for i in range(num_of_event):
    tmp_input = input().split(",") #the item in tmp_input is eventname, start time, end time, value of the event
    event = Event(tmp_input[0], tmp_input[1], tmp_input[2], tmp_input[3]) 
    #tmp_input[0] for event's name, tmp_input[1] for the start time, tmp_input[2] for the end time, tmp_input[3] for the value
    if calender.can_arrange(event) : #if calender can accept this event
        calender.add_event(event) #then append it 
    else:
        calender.deletionwho(event) #if calender can accept this event, we need to determine deleting the new event or now-existed events 

search_str = input()

find_word(search_str, calender)

