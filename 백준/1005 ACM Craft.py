import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

result = []

for _ in range(t):
    n, k = map(int,sys.stdin.readline().rstrip().split(' '))
    time = list(map(int,sys.stdin.readline().rstrip().split(' ')))

    time.insert(0,0)
    graph =[[] for _ in range(n+1)]

    x,y = map(int,sys.stdin.readline().rstrip().split(' '))
    graph[x].append(y)
    start = x

    for _ in range(k-1):
        x,y = map(int,sys.stdin.readline().rstrip().split(' '))
        graph[x].append(y)

    lastb = int(sys.stdin.readline().rstrip())

    queue = deque([[start, time[start]]])
    visited = [0 for _ in range(n+1)]
    visited[start] = time[start]
    while (True):
        now_b, now_time = queue.popleft()
        if now_b == lastb:
            break

        for i in graph[now_b]:
            if visited[i] == 0:
                visited[i] = now_time + time[i]
                queue.append([i,visited[i]])
            elif visited[i] < now_time + time[i]:
                visited[i] = now_time + time[i]
                queue.append([i,visited[i]])

    result.append(visited[lastb])

print(result)
