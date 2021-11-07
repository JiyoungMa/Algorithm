def bfs(start, n,graph,visited):
    from collections import deque
    queue =deque([start])
    visited[start] = 1
    
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            bfs(i,n,graph,visited)
    return answer
