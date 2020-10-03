HOUR_TO_MINUTES = 60

def timeConverter(hours, minutes):
    return hours * HOUR_TO_MINUTES + minutes

def time_to_string(time):
    return "{:02d}".format(time // HOUR_TO_MINUTES) + ":" + "{:02d}".format(time % HOUR_TO_MINUTES) 

def solution(n, t, m, timetable):
    answer = ''
    arrival_times = []
    bus_times = []
    bus_start = timeConverter(9, 0)
    last_bus_time, last_arrival_time = 0, 0
    available = True
    
    for time in timetable:
        hours, minutes = time.split(":")
        arrival_times.append(timeConverter(int(hours), int(minutes)))
        
    arrival_times.sort()
    
    for index in range(n):
        bus_times.append(bus_start + index * t)
       
    for bus_time in bus_times:
        passengers = 0
        available = True
        last_bus_time = bus_time
        for i in range(m):
            if arrival_times and arrival_times[0] <= bus_time:
                last_arrival_time = arrival_times[0]
                arrival_times.pop(0)
                passengers += 1
            else:
                break
        
        if passengers == m:
            available = False

    answer = time_to_string(last_arrival_time - 1) if not available \
        else time_to_string(last_bus_time)
    return answer

if __name__ == "__main__":
    test = 5
    
    if test == 1:
        n, t, m, timetable = 2, 10, 2, ["09:10", "09:09", "08:00"]
    elif test == 2:
        n, t, m, timetable = 10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    elif test == 3:
        n, t, m, timetable = 2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]
    elif test == 4:
        n, t, m, timetable = 1, 1, 1, ["23:59"]
    elif test == 5:
        n, t, m, timetable = 10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

    print(solution(n, t, m, timetable))