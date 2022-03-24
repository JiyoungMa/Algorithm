import sys
from collections import deque

input = sys.stdin.readline

answer = 0

w, h = map(int,input().rstrip().split(' '))

graph = []

for _ in range(h):
    graph.append(list(map(int,input().rstrip().split(' '))))

child = [[[] for _ in range(w)]for _ in range(h)]
visited = [[False for _ in range(w)]for _ in range(h)]

for y in range(h):
    for x in range(w):
        if graph[y][x] == 0 :
            if y-1>=0:
                if y % 2 == 0:
                    if graph[y-1][x] == 0:
                        child[y][x].append((x,y-1))
                    if x+1 < w and graph[y-1][x+1] == 0:
                        child[y][x].append((x+1,y-1))
                else:
                    if x-1 >= 0 and graph[y-1][x-1] == 0:
                        child[y][x].append((x-1,y-1))
                    if graph[y-1][x] == 0:
                        child[y][x].append((x,y-1))
            
            if y+1 < h:
                if y%2 == 0:
                    if graph[y+1][x] == 0:
                        child[y][x].append((x,y+1))
                    if x+1 < w and graph[y+1][x+1] == 0:
                        child[y][x].append((x+1,y+1))
                else:
                    if x-1 >= 0 and graph[y+1][x-1] == 0:
                        child[y][x].append((x-1,y+1))
                    if graph[y+1][x] == 0:
                        child[y][x].append((x,y+1))

            if x-1 >= 0:
                if graph[y][x-1] == 0:
                    child[y][x].append((x-1,y))

            if x+1 < w :
                if graph[y][x+1] == 0:
                    child[y][x].append((x+1,y))

def getCount(x,y):
    result = 0
    queue = deque([(x,y)])

    visited[y][x] = True

    while queue:
        dx,dy = queue.pop()

        now_minus = len(child[dy][dx])

        if dy == 0:
            if dx == 0:
                now_minus += 3
            elif dx == w-1:
                now_minus += 4
            else:
                now_minus += 2
        elif dy == h-1:
            if dy % 2 == 0:
                if dx == 0:
                    now_minus += 3
                elif dx == w-1:
                    now_minus += 4
                else:
                    now_minus += 2
            else:
                if dx == 0:
                    now_minus += 4
                elif dx == w-1 :
                    now_minus += 3
                else:
                    now_minus += 2
        else:
            if dy % 2== 1:
                if dx == 0:
                    now_minus += 3
                elif dx == w-1:
                    now_minus += 1
            else:
                if dx == 0:
                    now_minus += 1
                elif dx == w-1:
                    now_minus += 3
        result += 6 - now_minus

        for mx,my in child[dy][dx]:
            if visited[my][mx] == False:
                visited[my][mx] = True
                queue.append((mx,my))

    return result
                
nowy = 0
for nowx in range(w):
    if visited[nowy][nowx] == False and graph[nowy][nowx] == 0:
        answer += getCount(nowx,nowy)
    elif graph[nowy][nowx] == 1:
        if nowx == 0:
            answer += 3
        elif nowx == w-1:
            answer += 4
        else:
            answer += 2

nowy = h-1
for nowx in range(w):
    if visited[nowy][nowx] == False and graph[nowy][nowx] == 0:
        answer += getCount(nowx,nowy)
    elif graph[nowy][nowx] == 1:
        if (nowy%2 == 0 and nowx == 0) or (nowy%2 == 1 and nowx == w-1):
            answer += 3
        elif (nowy%2 == 0 and nowx == w-1) or (nowy%2 == 1 and nowx == 0):
            answer += 4
        else:
            answer += 2

nowx = 0
for nowy in range(1,h-1,1):
    if visited[nowy][nowx] == False and graph[nowy][nowx] == 0:
            answer += getCount(nowx,nowy)
    elif graph[nowy][nowx] == 1:
        if nowy % 2 == 0:
            answer += 1
        else:
            answer += 3

nowx = w-1
for nowy in range(1,h-1,1):
    if visited[nowy][nowx] == False and graph[nowy][nowx] == 0:
            answer += getCount(nowx,nowy)
    elif graph[nowy][nowx] == 1:
        if nowy % 2 == 1:
            answer += 1
        else:
            answer += 3


print(answer)
