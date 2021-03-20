import sys
from itertools import combinations
import copy

def spread_spaces(g,x,y):
    px = [0,0,-1,1]
    py = [-1,1,0,0]

    for i in range(4):
        nx = x+px[i]
        ny = y+py[i]

        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        if g[ny][nx] == 0:
            g[ny][nx] = 2
            g = spread_spaces(g,nx,ny)
    
    return g

def count_spaces(g):
    count = 0
    for i in range(n):
        count += g[i].count(0)

    return count

    
n,m = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

walls = []
germs = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append([i,j])
        elif graph[i][j] == 2:
            germs.append([i,j])

comb = list(combinations(walls,3))

maximum = 0
for w in comb:
    g = copy.deepcopy(graph)

    for y,x in w:
        g[y][x] = 1

    for y,x in germs:
        g = spread_spaces(g,x,y)

    result = count_spaces(g)
    if result > maximum:
        maximum = result

print(maximum)
        