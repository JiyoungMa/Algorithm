import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n,k = map(int, input().rstrip().split())
    times = list(map(int,input().rstrip().split()))
    max_times = [0 for _ in range(n+1)]

    times.insert(0,0)
    graph_in = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        x,y = map(int,input().rstrip().split())
        graph_in[y] += 1
        graph[x].append(y)

    w = int(input().rstrip())

    queue = deque([])

    for i in range(1,n+1):
        if graph_in[i] == 0:
            queue.append(i)
            max_times[i] = times[i]

    result = 0

    while queue:
        now_i = queue.popleft()

        if now_i ==w:
            break

        for next in graph[now_i]:
            graph_in[next] -= 1
            max_times[next] = max(max_times[next],max_times[now_i] + times[next])
            if graph_in[next]==0:
                queue.append(next)


    print(max_times[w])
