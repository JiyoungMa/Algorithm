import sys

n,m = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

s,x,y = map(int, sys.stdin.readline().rstrip().split(' '))

for i in range(s):
    blank = []
    for yy in range(n):
        ind = -1
        blank_n = []
        c = graph[yy].count(0)
        for i in range(c):
            ind = graph[yy].index(0,ind+1)
            blank_n.append(ind)
        blank.append(blank_n)
    
    change_graph = []
    for yy in range(n):
        blank_n = blank[yy]
        for xx in blank_n:
            germs = []
            positions = [[yy-1,xx],[yy+1,xx], [yy,xx-1], [yy,xx+1]]

            for ny,nx in positions:
                if ny<0 or ny>=n or nx<0 or nx>=n:
                    continue
                else:
                    if graph[ny][nx] != 0:
                        germs.append(graph[ny][nx])
            if len(germs) != 0:
                change_graph.append([yy,xx,min(germs)])

    for yy,xx, mi in change_graph:
        graph[yy][xx] = mi

print(graph[x-1][y-1])
