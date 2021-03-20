import sys

n,m = map(int,sys.stdin.readline().rstrip().split(' '))
papers = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

graph = []
maximum = -1

for _ in range(k):
    x,y = map(int,sys.stdin.readline().rstrip().split(' '))
    if x>maximum:
        maximum = x
    graph.append(y)

m = maximum
graph.sort()
while(True):
    copied_graph = graph[:]
    for _ in range(papers):
        now = copied_graph[0] + m
        copied_graph = [g for g in copied_graph if g>=now]
        if len(copied_graph) == 0:
            break
    if len(copied_graph) == 0:
        print(m)
        break
    else:
        m += 1
    