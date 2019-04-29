from datetime import datetime, timedelta
year = input()

#mothersday
datetime_obj = datetime.strptime(year+", 5", "%Y, %m")
if (datetime_obj.weekday() != 6):

    day_delta = 6 - datetime_obj.weekday() if 6 - datetime_obj.weekday() >= 0 else 6 - datetime_obj.weekday() + 7
    datetime_obj += timedelta(days = day_delta) 
else:
    pass
datetime_obj += timedelta(days = 7)
datetime_obj = datetime_obj.date()
print("MOTHERS_DAY", datetime_obj)


#grandparentsday
datetime_obj = datetime.strptime(year+", 8", "%Y, %m")
if (datetime_obj.weekday() != 6):
    day_delta = 6 - datetime_obj.weekday() if 6 - datetime_obj.weekday() >= 0 else 6 - datetime_obj.weekday() + 7
    datetime_obj += timedelta(days = day_delta) 
else:
    pass
datetime_obj += timedelta(days = 7*3)
datetime_obj = datetime_obj.date()
print("GRANDPARENTS_DAY", datetime_obj)


#ATAYALS_DAY
datetime_obj = datetime.strptime(year+", 8", "%Y, %m")
if (datetime_obj.weekday() != 4):
    day_delta = 4 - datetime_obj.weekday() if 4 - datetime_obj.weekday() >= 0 else 4 - datetime_obj.weekday() + 7
    datetime_obj += timedelta(days = day_delta) 
else:
    pass

while(datetime_obj.month == 8):
    datetime_obj += timedelta(days = 7)
else:
    datetime_obj -= timedelta(days = 7)
datetime_obj = datetime_obj.date()
print("ATAYALS_DAY", datetime_obj)


#SAKIZAYAS_DAY
datetime_obj = datetime.strptime(year+", 10", "%Y, %m")
if (datetime_obj.weekday() != 4):
    day_delta = 4 - datetime_obj.weekday() if 4 - datetime_obj.weekday() >= 0 else 4 - datetime_obj.weekday() + 7
    datetime_obj += timedelta(days = day_delta) 
else:
    pass
datetime_obj = datetime_obj.date()
print("SAKIZAYAS_DAY", datetime_obj)


#MLKINGS_DAY
datetime_obj = datetime.strptime(year+", 1", "%Y, %m")
if (datetime_obj.weekday() != 0):
    day_delta = 0 - datetime_obj.weekday() if 0 - datetime_obj.weekday() >= 0 else 0 - datetime_obj.weekday() + 7
    datetime_obj += timedelta(days = day_delta) 
else:
    pass
datetime_obj += timedelta(days = 7*2)
datetime_obj = datetime_obj.date()
print("MLKINGS_DAY", datetime_obj)