from collections import deque
def solution(s):
    answer = True
    queue = deque([])
    
    for i in s:
        if i == "(":
            queue.append(i)
        else:
            if len(queue)==0:
                answer = False
                break
            check = queue.pop()
            
    if len(queue) != 0:
        answer = False
    return answer
