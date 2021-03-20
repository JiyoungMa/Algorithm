import sys
from collections import deque

k = int(sys.stdin.readline().rstrip())
w,h = map(int,sys.stdin.readline().rstrip().split(' '))
group = []
for _ in range(h):
    group.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]

def bfs():
    moving_k = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
    moving = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([[0,0,0]])
    visited[0][0][0] = 0
    while queue:
        now_x, now_y, k_count= queue.popleft()
        count = visited[now_y][now_x][k_count]

        if now_x == w-1 and now_y == h-1:
            print(visited[now_y][now_x][k_count])
            return

        if k_count +1 <= k:
            for mx, my in moving_k:
                nx = now_x + mx
                ny = now_y + my

                if nx<0 or nx>=w or ny<0 or ny>=h:
                    continue
                
                if group[ny][nx] == 0 and visited[ny][nx][k_count+1] == 0:
                    visited[ny][nx][k_count+1] = count +1
                    queue.append([nx,ny,k_count+1])

        for mx, my in moving:
            nx = now_x + mx
            ny = now_y + my

            if nx<0 or nx>=w or ny<0 or ny>=h:
                continue

            if group[ny][nx] == 0 and visited[ny][nx][k_count] == 0:
                visited[ny][nx][k_count] = count +1
                queue.append([nx,ny,k_count])
    print(-1)

bfs()