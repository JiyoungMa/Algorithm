import sys
from collections import deque
#BFS

n,m,k,x = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []
for i in range(n+2):
    graph.append([])

shortest = [n] * (n+1)
for i in range(m):
    xx,y = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[xx].append(y)

visited = [False]*(n+1)

queue = deque([(x,0)])

while queue:
    now, distance = queue.popleft()

    if shortest[now] > distance:
        shortest[now] = distance

    visited[now] = True

    for i in graph[now]:
        if shortest[i] > distance:
            queue.append((i,distance +1))

if shortest.count(k) == 0:
    print(-1)
else:
    for i in range(len(shortest)):
        if shortest[i] == k:
            print(i)
