HOUR_TO_MINUTES = 60
SHARP = "#"

def string_to_time(hours, minutes):
    return hours * HOUR_TO_MINUTES + minutes

def time_to_string(time):
    return "{:02d}".format(time // HOUR_TO_MINUTES) + ":" + "{:02d}".format(time % HOUR_TO_MINUTES) 

# C, C#, D, D#, E, F, F#, G, G#, A, A#, B
def solution(m, musicinfos):
    answer = "(None)"
    musics = []
    max_duration = -0xFFFF
    processed_m = ""
    m = list(m)
    m.append(None)
    for pinch1, _next in zip(m, m[1:]):
        if pinch1 == SHARP:
            continue
        
        if _next == SHARP:
            # convert to lowercase
            pinch1 = chr(ord(pinch1) - ord('A') + ord('a'))

        processed_m += pinch1
        
    #print(m, "m:", processed_m)
    # 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다
    for info in musicinfos:
        start, end, title, song = info.split(",")
        start = string_to_time(*list(map(int, start.split(":"))))
        end = string_to_time(*list(map(int, end.split(":"))))
        duration = end - start
        
        len_of_song = len(song)
        song = list(song)
        song.append(None)
        real_song = ""
        played = ""
        
        for pinch1, _next in zip(song, song[1:]):
            if pinch1 == SHARP:
                len_of_song -= 1
                continue
            
            if _next == SHARP:
                # convert to lowercase
                pinch1 = chr(ord(pinch1) - ord('A') + ord('a'))

            real_song += pinch1
            
        for i in range(duration):
            played += real_song[i % len_of_song]

        #print(title) 
        #print(real_song)           
        #print(played)
        #print(m)
        #print(processed_m)
        #print()    
        
        if max_duration < duration and processed_m in played:
            answer = title
            max_duration = duration
            
    return answer

if __name__ == "__main__":

    test = 4
    
    if test == 1:
        m, musicinfos = "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    if test == 2:
        m, musicinfos = "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    
    if test == 3:
        m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    
    if test == 4:
        m, musicinfos = "C#", ["03:00,03:30,FOO,CC#B", "03:00,03:30,BAR, CC#BCC#BCC#B"]

    print(solution(m, musicinfos[:-1]))
