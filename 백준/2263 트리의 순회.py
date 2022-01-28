import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

inorder = list(map(int,input().rstrip().split()))
postorder = list(map(int,input().rstrip().split()))

index_list = [None for _ in range(n+1)]

for i in range(n):
    index_list[postorder[i]] = i

queue = []
heapq.heappush(queue,[-1,inorder])

while queue:
    i, now_list = heapq.heappop(queue)

    now_root = postorder[max([index_list[i] for i in now_list])]
    print(now_root,end = ' ')
    root_index = now_list.index(now_root)
    if root_index != 0:
        heapq.heappush(queue,[i*2,now_list[:root_index]])
    if root_index != n-1:
        heapq.heappush(queue,[i*2+1,now_list[root_index+1:]])
