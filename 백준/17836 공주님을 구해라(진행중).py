import sys
from collections import deque

input = sys.stdin.readline
move = [(0,1), (0,-1), (1,0),(-1,0)]

n,m,t = map(int, input().rstrip().split(' '))
board = []

for _ in range(n):
    board.append(list(map(int,input().rstrip().split(' '))))


queue = deque([[1,0,0,0]])

visited = [[0 for _ in range(m)] for _ in range(n)]
sword_visit = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

answer = -1

sword = False

while queue:
    now_time, now_sword, now_x, now_y = queue.popleft()

    if now_time > t:
        continue

    if now_x == m-1 and now_y == n-1:
        answer = now_time - 1
        break

    for mx,my in move:
        dx = now_x + mx
        dy = now_y + my

        if dx<0 or dx>=m or dy<0 or dy>=n :
            continue

        if now_sword == 1 and (visited[dy][dx] == 0 or visited[dy][dx] == now_time + 1):
            visited[dy][dx] = now_time + 1
            queue.append([now_time+1, now_sword, dx,dy])
        elif now_sword == 0 and sword_visit[dy][dx] == True:
            continue
        elif now_sword == 0 and visited[dy][dx] == 0:
            if board[dy][dx] == 0 :
                visited[dy][dx] = now_time + 1
                queue.append([now_time+1, now_sword, dx,dy])
            elif board[dy][dx] == 2:
                sword_visit[dy][dx] = True
                visited[dy][dx] = now_time + 1
                queue.append([now_time+1, 1, dx,dy])

if answer == -1:
    print("Fail")
else:
    print(answer)
