import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

graph = [[] for _ in range(n+1)]

start,end = map(int,input().rstrip().split())

m = int(input().rstrip())

for _ in range(m):
    x,y = map(int,input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([start])
visitied = [-1] * (n+1)
visitied[start] = 0

while queue:
    now = queue.popleft()

    for next in graph[now]:
        if visitied[next] == -1 or visitied[next] > visitied[now] + 1:
            visitied[next] = visitied[now] + 1
            queue.append(next)

print(visitied[end])
