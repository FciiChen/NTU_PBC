import copy

class Time():

    def __init__(self, h, m, s): #constructor __init__ 
        self.hour = h
        self.minute = m
        self.second = s

    def print_nicely(self):
        print("%02d:%02d:%02d" %(self.hour, self.minute, self.second) , end = "")

class Event():
    def __init__(self, name, t1, t2):
        self.name = name
        self.start = t1
        self.end = t2
        
    def set_name(self, n):
        self.name = n

    def print_nicely(self):
        print("%s : from " %self.name, end = "")
        self.start.print_nicely()
        print(" to ", end = "")
        self.end.print_nicely()

class Schedule():
    def __init__(self):
        self.now_event = []

    def add_event(self, e):
        self.now_event.append(e)

    def print_events(self):
        for item in self.now_event:
            item.print_nicely()
            print()


name = 'PBC'
t1 = Time(9, 10, 0)
t2 = Time(12, 10, 0)
e1 = Event(name, t1, t2)

t1 = Time(14, 10, 0)
t2 = Time(17, 10, 0)
e2 = Event("tsetclass", t1, t2)

sch = Schedule()
sch.add_event(e1)
sch.add_event(e2)
sch.print_events()

''' copy.deepcopy(multiple type object)
e2 = copy.deepcopy(e1)
print()
e2.print_nicely()
'''



