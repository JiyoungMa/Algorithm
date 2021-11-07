import heapq
def solution(m, musicinfos):
    answer = []
    
    for music in range(len(musicinfos)):
        start_time,end_time,song_name, plays = musicinfos[music].split(",")
        played = ""
        start_time = list(map(int,start_time.split(":")))
        end_time = list(map(int,end_time.split(":")))
        start_time = start_time[0]*60 + start_time[1]
        end_time = end_time[0]*60 + end_time[1]
        
        playtime = end_time-start_time
        plays_playtime = len(plays) - plays.count("#")
        while playtime>=plays_playtime:
            played += plays
            playtime -= plays_playtime
            
        p_index = 0
        for _ in range(playtime):
            if plays[p_index+1] == "#":
                p_index += 1
            p_index += 1
            
        played += plays[:p_index+1]
        
        for i in range(len(played)-len(m)):
            temp = played[i:i+len(m)]
            if temp == m and played[i+len(m)] != "#":
                heapq.heappush(answer,[-(end_time-start_time),music,song_name])
                break
    if len(answer) == 0:
        return "(None)"
    else:
        now = heapq.heappop(answer)
        return now[2]
