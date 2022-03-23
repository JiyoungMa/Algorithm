import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

answer = 0
graph = [[] for _ in range(n+1)]
graph[0] = [1,1]
parents = [0]*(n+1)
visited = [False] * (n+1)
count_visit = 0

for _ in range(n):
    a,b,c = map(int,input().rstrip().split(' '))
    graph[a] = [b,c]
    
    if b != -1:
        parents[b] = a

    if c != -1:
        parents[c] = a

def inorderTraverse():
    now = 1
    while True:

        left,right = graph[now]

        if right != -1 :
            now = right
        else:
            return now

end = inorderTraverse()

queue = deque([1])

while queue:
    now = queue.popleft()

    if visited[now] == False:
        visited[now] = True
        count_visit += 1
    
    if count_visit == n and now == end:
        break

    answer += 1
    left_node, right_node = graph[now]

    if left_node != -1 and visited[left_node] == False:
        queue.append(left_node)
    elif right_node != -1 and visited[right_node] == False:
        queue.append(right_node)
    else:
        queue.append(parents[now])

print(answer)
