from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    if begin not in words:
        words.append(begin)
    
    graph=[[] for _ in range(len(words))]
    visitied = [0] * len(words)
    for i in range(len(words)):
        for j in range(len(words)):
            if j == i :
                continue
            count = 0
            for c in range(len(words[i])):
                if words[i][c] != words[j][c]:
                    count+=1
                    
            if count == 1:
                graph[i].append(j)
                
    begin = words.index(begin)
    target = words.index(target)
    
    queue = deque([begin])
    visitied[begin] = 1
    
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visitied[i] == 0:
                visitied[i] = visitied[now] + 1
                queue.append(i)
                
    return visitied[target] -1
