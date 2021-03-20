import sys
from collections import deque


def bfs(graph,now_x,now_y,dx,dy):
    moving= [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
    queue = deque([[now_y, now_x]])
    while queue:
        y,x = queue.popleft()
        for my,mx in moving:
            ny = y+my
            nx = x+mx

            if ny<0 or ny>=len(graph) or  nx<0 or nx>= len(graph[0]):
                continue

            next = graph[y][x] + 1

            if next < graph[ny][nx] or graph[ny][nx]==0:
                graph[ny][nx] = next
                queue.append([ny,nx])

        if graph[dy][dx] != 0:
            break

    return graph


n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    size = int(sys.stdin.readline().rstrip())
    now_x, now_y = map(int,sys.stdin.readline().rstrip().split(' '))
    dx, dy = map(int,sys.stdin.readline().rstrip().split(' '))

    graph = [[0 for i in range(size)] for j in range(size)]
    graph[now_y][now_x] = 1
    graph = bfs(graph,now_x,now_y,dx,dy)
    print(graph[dy][dx]-1)