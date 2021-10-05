import sys
import heapq
input = sys.stdin.readline

m,n = map(int, input().rstrip().split())
maps = []
queue = []
visited = [[0 for _ in range(m)] for _ in range(n)]

moves = [(1,0), (-1,0), (0,1), (0,-1)]

for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))

for y in range(n):
    for x in range(m):
        if maps[y][x] == 1:
            heapq.heappush(queue,(1,y,x))
            visited[y][x] = 1
        if maps[y][x] == -1:
            visited[y][x] = -1

def dfs():
    while queue:
        days, nowy, nowx = heapq.heappop(queue)

        if visited[nowy][nowx] < days:
            continue

        for my,mx in moves:
            dy = nowy + my
            dx = nowx + mx

            if dy<0 or dy>=n or dx<0 or dx>=m:
                continue

            if maps[dy][dx] == -1 :
                continue

            if visited[dy][dx] == 0:
                visited[dy][dx] = days + 1
                heapq.heappush(queue,(days+1,dy,dx))

if len(queue) == n*m:
    print(0)
else:
    dfs()

    boolCheck = True
    maximum = -1

    for y in range(n):
        if 0 in visited[y]:
            boolCheck = False
            break
        maximum = max(maximum, max(visited[y]))

    if boolCheck == False:
        print(-1)
    else:
        print(maximum-1)
