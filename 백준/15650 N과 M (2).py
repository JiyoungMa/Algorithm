n,m= input().split(' ')
n = int(n)
m = int(m)

def DFS(graph,start_node,visit) :
    global m
    if len(visit) < m:
        children = graph[start_node]
        for node in children:
            if node not in visit and node > visit[len(visit)-1]:
                DFS(graph,start_node,visit+[node])
            
    else:
        for i in visit:
            print(i,end=' ')
        print()
        


graph = dict()
for i in range(n):
    graph[i+1] = [a+1 for a in range(i,n,1)]

for i in range(1,n+1,1):
    visit = [i]
    DFS(graph,i,visit)
   

