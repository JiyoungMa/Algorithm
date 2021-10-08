from collections import deque
def solution(s):
    answer = 0
    right = ["(","[","{"]
    left = [")","]","}"]
    for i in range(len(s)):
        stack = deque([])
        strs = deque(list(s[:]))
        result = True
        while strs:
            now = strs.popleft()
            
            if now in left:
                now_index = left.index(now)
                if len(stack) > 0:
                    check = stack.pop()
                    if check != right[now_index]:
                        result = False
                        break
                else:
                    result = False
                    break
            elif now in right:
                stack.append(now)
        
        if len(strs) != 0 or len(stack) != 0:
            result = False
        
        if result == True:
            answer += 1
            
        s = s[1:] + s[0]
                    
    return answer
