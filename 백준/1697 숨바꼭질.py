import sys
from collections import deque

now,des = map(int,sys.stdin.readline().rstrip().split(' '))

visited = [0] * 200002
visited[now] = 1

queue = deque([now])
while queue:
    now = queue.popleft()
    count = visited[now] + 1
    next_p = now - 1
    if next_p >=0 and next_p < 200002 and visited[next_p] == 0:
        visited[next_p] = count
        queue.append(next_p)

    next_p = now +1
    if next_p >=0 and next_p < 200002 and visited[next_p] == 0:
        visited[next_p] = count
        queue.append(next_p)

    next_p = now *2
    if next_p >=0 and next_p < 200002 and visited[next_p] == 0:
        visited[next_p] = count
        queue.append(next_p)

    if visited[des] != 0:
        break

print(visited[des]-1)
    