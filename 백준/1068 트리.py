import sys
from collections import deque

input = sys.stdin.readline

node_num = int(input().rstrip())

parents_node = list(map(int, input().rstrip().split(' ')))

remove_node = int(input().rstrip())

graph = [[] for i in range(node_num)]

queue = deque([])

visited = [False] * len(parents_node)

for i in range(len(parents_node)):
    if parents_node[i] == -1:
        queue.append(i)
    else:
        graph[parents_node[i]].append(i)

answer = 0

while queue:
    now = queue.popleft()

    visited[now] = True

    if now == remove_node:
        continue

    if len(graph[now]) == 0 or graph[now] == [remove_node]:
        answer += 1

    else:
        for i in graph[now]:
            if visited[i] == False:
                queue.append(i)

print(answer)
