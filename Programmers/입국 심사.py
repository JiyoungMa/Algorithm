def solution(n, times):
    from queue import PriorityQueue
    time_count= PriorityQueue()
    for i in times:
        time_count.put([1,i])
    
    while time_count:
        c,t = time_count.get()
        
        while time_count.get()[0] == c:
            continue
        if c == n:
            return t
        
        for i in times:
            time_count.put([c+1, t+i])
