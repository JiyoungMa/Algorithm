import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

routes = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    routes[b] += 1

queue = deque([])

visitied = [0] * (n+1)

for i in range(1,n+1):
    if routes[i] == 0:
        visitied[i] = 1
        queue.append(i)

while queue:
    now = queue.popleft()

    for i in graph[now]:
        visitied[i] = visitied[now] + 1
        routes[i] -= 1
        if routes[i] == 0:
            queue.append(i)

for i in range(1,n+1):
    print(visitied[i], end =' ')
