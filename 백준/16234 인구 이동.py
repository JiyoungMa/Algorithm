import sys

sys.setrecursionlimit(1000000)
n,l,r = map(int,sys.stdin.readline().rstrip().split(' '))

graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

count = 0

px = [0,0,1,-1]
py = [1,-1,0,0]

def dfs(lands,x,y):
    for i in range(4):
        dx = x+px[i]
        dy = y+py[i]

        if dx<0 or dx>=n or dy<0 or dy>=n:
            continue
        
        m = abs(graph[y][x] - graph[dy][dx])

        if m>= l and m<= r and [dx,dy] not in lands:
            lands.append([dx,dy])
            lands = dfs(lands,dx,dy)

    return lands

while(True):
    land_list = []
    land_elements = []

    for y in range(n):
        for x in range(n):
            if [x,y] not in land_elements:
                return_list = dfs([[x,y]],x,y)
                if return_list != [[x,y]]:
                    land_list.append(return_list)
                    land_elements.extend(return_list)

    if land_list == []:
        break

    count += 1
    for land in land_list:
        sums = 0
        for x,y in land:
            sums += graph[y][x]

        divided = sums // len(land)
        for x,y in land:
            graph[y][x] = divided

print(count)
