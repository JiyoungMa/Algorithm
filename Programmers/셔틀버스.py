import datetime
from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    timedelta_str = "2021-10-08 T 09:00:00"
    start_time = datetime.datetime.strptime(timedelta_str,"%Y-%m-%d T %H:%M:%S")
    timetable.sort()
    timetable = deque(timetable)
    time_front = "2021-10-08 T "
    buses = []
    
    for i in range(n):
        buses.append(start_time+datetime.timedelta(minutes = t*i))
    
    success = [[] for _ in range(len(buses))]
    
    for b in range(len(buses)):
        for i in range(m):
            if timetable:
                passenger = timetable[0]

                passenger_time = datetime.datetime.strptime(time_front + passenger+":00","%Y-%m-%d T %H:%M:%S")
                if buses[b] >= passenger_time:
                    success[b].append(passenger_time)
                    timetable.popleft()
                else:
                    break
    print(success)
    f= False
    
    if len(success[-1]) < m:
        f = True
        answer = buses[-1].strftime("%H:%M")
    else:
        success[-1].sort()
        answer = (success[-1][-1] - datetime.timedelta(minutes=1)).strftime("%H:%M")
    
    return answer
