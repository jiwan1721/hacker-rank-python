from datetime import datetime
import time
# start_time = time.time()
# print(start_time)
# end_time = time.time()
# print(end_time-start_time)

# start_time = datetime.now()
start_time = time.localtime()
current_time = time.strftime("%H:%M:%S",start_time)
print(current_time)

def time_deff(start_t,end_t):
    time1 = datetime.strptime(start_t, "%H:%M")
    time2 = datetime.strptime(end_t, "%H:%M")
    difference_time = time2-time1
    return difference_time


print(time_deff('10:34', "7:19"))