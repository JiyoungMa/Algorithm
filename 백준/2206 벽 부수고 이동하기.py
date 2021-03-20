import sys
import copy
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split(' '))

graph = []

walls = []
for i in range(n):
    input_list = list(map(int,list(sys.stdin.readline().rstrip())))
    for j in range(m):
        if input_list[j] == 1:
            walls.append([i,j])
    graph.append(input_list)

visited = [[[0] * 2 for i in range(m)] for i in range(n)]
visited[0][0][0] = 1 #0이 벽을 안뚫은 상태
minimum = 1000000

def bfs():
    moving = [[1,0], [-1,0], [0,1], [0,-1]]
    queue = deque([[0,0,0]])

    while queue:
        y,x,i = queue.popleft()

        for my, mx in moving:
            dy = my+y
            dx = mx+x

            if dy<0 or dy>=n or dx<0 or dx>=m:
                continue

            if graph[dy][dx]==0 and visited[dy][dx][i] == 0:
                visited[dy][dx][i] = visited[y][x][i] +1
                queue.append([dy,dx,i])

            elif graph[dy][dx] == 1 and i == 0 and visited[dy][dx][1] == 0:
                visited[dy][dx][1] = visited[y][x][0] +1
                queue.append([dy,dx,1])

        if visited[n-1][m-1][0] !=0 and visited[n-1][m-1][1] != 0:
            break

bfs()
if visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0:
    print(-1)
elif visited[n-1][m-1][0] ==0 and visited[n-1][m-1][1] != 0:
    print(visited[n-1][m-1][1])
elif visited[n-1][m-1][0] != 0 and visited[n-1][m-1][1] == 0:
    print(visited[n-1][m-1][0])
elif visited[n-1][m-1][0] > visited[n-1][m-1][1]:
    print(visited[n-1][m-1][1])
else:
    print(visited[n-1][m-1][0])