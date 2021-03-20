import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []

for i in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

queue = deque([(0,0)])

dx = [1,0, -1,0]
dy = [0, 1, 0, -1]

while queue:
    x,y = queue.popleft()
    if x==m-1 and y ==n-1:
        break
    for i in range(4):
        next_x = x+dx[i]
        next_y = y +dy[i]

        if next_x <0 or next_x>=m or next_y<0 or next_y>=n:
            continue
        if graph[next_y][next_x] == 1:
            graph[next_y][next_x] = graph[y][x] + 1
            queue.append((next_x,next_y))
            break

print(graph[n-1][m-1])