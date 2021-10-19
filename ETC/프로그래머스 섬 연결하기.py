import heapq
def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    answer = 0
    queue = []
    parent = [i for i in range(n)]
    
    for a,b,c in costs:
        heapq.heappush(queue,[c,a,b])
        
    while queue:
        length, a, b = heapq.heappop(queue)
        
        if find_parent(parent,a) != find_parent(parent,b):
            answer += length
            union_parent(parent,a,b)
        
    return answer
