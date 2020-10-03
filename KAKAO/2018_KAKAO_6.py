import re

HOUR_TO_MS = 60 * 60 * 1000
MINUTE_TO_MS = 60 * 1000
S_TO_MS = 1000

def convert_time(hours, minutes, seconds, mili_seconds):
    return hours * HOUR_TO_MS + minutes * MINUTE_TO_MS + seconds * S_TO_MS + mili_seconds

def solution(lines):
    answer = 0
    times = []
    max_processed = 0
    max_start_time = 0
    max_end_time = 0
    result = []

    for line in lines:
        time, duration = line.split()[1:]
        h_m_s = re.search("([0-4][0-9]):([0-6][0-9]):([0-6][0-9])", time).groups()
        ms = re.search("\.([0-9][0-9][0-9])", time).group(1)
        h_m_s_ms = h_m_s + (ms, )
        duration = int(float(duration[:-1]) * S_TO_MS) 
        end_time = convert_time(*list(map(int, h_m_s_ms)))
        start_time = end_time - duration + 1
        times.append((start_time, end_time))
    
    times.sort()
    
    for index in range(len(times)):
        section_start = times[index][0]
        count = 0
        section_end = section_start + S_TO_MS - 1
        for time in times:
            if section_start <= time[0] <= section_end or \
                section_start <= time[1] <= section_end or \
                (time[0] <= section_start <= time[1] and \
                    time[0] <= section_end <= time[1]):
                count += 1
    
        if max_processed < count:
            max_processed = count
    
    for index in range(len(times)):
        section_start = times[index][1]
        count = 0
        section_end = section_start + S_TO_MS - 1
        for time in times:
            if section_start <= time[0] <= section_end or \
                section_start <= time[1] <= section_end or \
                (time[0] <= section_start <= time[1] and \
                    time[0] <= section_end <= time[1]):
                count += 1
                
        if max_processed < count:
            max_processed = count    
            
    answer = max_processed
    return answer


if __name__ == "__main__":

    
    lines =  ["2016-09-15 01:00:04.002 2.999s",
                "2016-09-15 01:00:04.002 2.999s"]
    
    print(solution(lines))