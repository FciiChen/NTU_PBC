class Time():

    hourIn12 = True #class static use "Time" to call. For example, Time.hourIn12

    def __init__(self, h, m, s): #constructor __init__ 
        self.hour = h
        self.minute = m
        self.second = s

    def is_earlier_than(self, t):
        if (self.hour*3600+self.minute*60+self.second) < (t.hour*3600+t.minute*60+t.second):
            return True;
        else:
            return False;

    def print_normally(self):
        print("%d:%d:%d" %(self.hour, self.minute, self.second), end = "")

    def print_nicely(self):

        print("%02d:%02d:%02d" %(self.hour, self.minute, self.second))
    
    @classmethod
    def set_hourIn12(cls, h12): #cls for classmethed for changing class attribution
        cls.hourIn12 = h12







keyin = input().split(" ")
keyin = [int(i) for i in keyin]

t1 = Time(keyin[0], keyin[1], keyin[2])
t2 = Time(keyin[3], keyin[4], keyin[5])
t3 = Time(keyin[6], keyin[7], keyin[8])

'''
#t1.print_nicely()
print(Time.hourIn12)
Time.set_hourIn12(False)
print(Time.hourIn12)
#t2.print_nicely()
'''



''' 
if t1.is_earlier_than(t2):
    if t3.is_earlier_than(t1):
        t3.print_nicely()
    else:
        t1.print_nicely()
else:
    if t3.is_earlier_than(t2):
        t3.print_nicely() 
    else:
        t2.print_nicely()
'''