import sys
from itertools import combinations
import copy

n = int(sys.stdin.readline().rstrip())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip().split(' ')))

objects = []
students = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            objects.append([i,j])
        elif graph[i][j] == 'S':
            students.append([i,j])

o_list = list(combinations(objects,3))

b = True

for o in o_list:
    b = True
    g = copy.deepcopy(graph)

    for y,x in o:
        g[y][x] = 'O'
    

    for y,x in students:
        for xx in range(x,n,1):
            if g[y][xx] == 'O':
                b = True
                break
            elif g[y][xx] == 'T':
                b = False
                break
        
        if b== False:
            break

        for xx in range(x,-1, -1):
            if g[y][xx] == 'O':
                b = True
                break
            elif g[y][xx] == 'T':
                b = False
                break

        if b== False:
            break

        for yy in range(y,n,1):
            if g[yy][x] == 'O':
                b = True
                break
            elif g[yy][x] == 'T':
                b= False
                break
        
        if b== False:
            break

        for yy in range(y,-1,-1):
            if g[yy][x] == 'O':
                b = True
                break
            elif g[yy][x] == 'T':
                b= False
                break
        
        if b== False:
            break

    if b == False:
        continue
    if b == True:
        break

if b== True:
    print("YES",end = '')
else:
    print("NO", end = '')
