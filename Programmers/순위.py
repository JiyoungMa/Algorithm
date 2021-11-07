def solution(n, results):
    answer = 0
    win_graph = [set() for _ in range(n+1)]
    loose_graph = [set() for _ in range(n+1)]
    
    for a,b in results:
        win_graph[a].add(b)
        loose_graph[b].add(a)
        
    for i in range(1,n+1):
        for w in win_graph[i]:
            loose_graph[w].update(loose_graph[i])
        for l in loose_graph[i]:
            win_graph[l].update(win_graph[i])

    for i in range(1,n+1):
        if len(loose_graph[i]) + len(win_graph[i]) == n-1:
            answer += 1


    return answer
