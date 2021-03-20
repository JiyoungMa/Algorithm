import sys

n,m = map(int, sys.stdin.readline().rstrip().split(' '))
group = [[[] for _ in range(n)] for _ in range(m)]
moving = [[1,0],[-1,0],[0,1],[0,-1]]
walls = []
for y in range(m):
    input_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    for x in range(n):
        for mx, my in moving:
            nx,ny = x+mx, y+my
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            group[y][x].append([nx,ny])

        if input_list[x] >=8 :
            input_list[x] -= 8
            ny = y+1
            if ny<m:
                group[y][x].remove([x,ny])
                walls.append([x,y,x,ny])

        if input_list[x] >= 4 :
            input_list[x] -= 4
            nx = x+1
            if nx<n:
                group[y][x].remove([nx,y])
                walls.append([x,y,nx,y])

        if input_list[x] >= 2:
            input_list[x] -= 2
            ny = y-1
            if ny>=0 :
                group[y][x].remove([x,ny])
                walls.append([x,y,x,ny])

        if input_list[x] >= 1:
            nx = x-1
            if nx>= 0:
                group[y][x].remove([nx,y])
                walls.append([x,y,nx,y])

wall_list = []
visited = [[False]*n for _ in range(m)]

def dfs(now_x, now_y, w):
    visited[now_y][now_x] = True
    wall_list[w].append([now_x,now_y])
    for nx,ny in group[now_y][now_x]:
        if not visited[ny][nx]:
            dfs(nx,ny,w)

    group[now_y][now_x] = []

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            wall_list.append([])
            w = len(wall_list)-1
            dfs(x,y,w)

print(len(wall_list))
maximum = 0
for i in wall_list:
    if len(i) > maximum:
        maximum = len(i)
print(maximum)

maximum = 0

for x,y,nx,ny in walls:
    now_w = -1
    next_w = -1
    for l in range(len(wall_list)):
        if [x,y] in wall_list[l]:
            now_w = l
        if [nx,ny] in wall_list[l]:
            next_w = l
        if now_w != -1 and next_w != -1:
            break

    if now_w != next_w and len(wall_list[now_w]) + len(wall_list[next_w]) > maximum:
        maximum = len(wall_list[now_w]) + len(wall_list[next_w])

print(maximum)
