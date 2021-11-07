def bfs(n, graph):
    from collections import deque
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    queue = deque([1])
    
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)
    
    maximum = max(visited)
    
    return visited.count(maximum)

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    answer = bfs(n,graph)
    return answer
