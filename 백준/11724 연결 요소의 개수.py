import sys
sys.setrecursionlimit(1000000)

n,m = map(int,sys.stdin.readline().rstrip().split(' '))

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(graph,start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

count = 0

for i in range(1,n+1,1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)

print(count)    