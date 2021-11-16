from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    
    queue = deque([[0,prices[0]]])
    
    for i in range(1,len(prices)):
        if prices[i] < queue[-1][1]:
            while queue and prices[i] < queue[-1][1]:
                nowi, value = queue.pop()
                answer[nowi] = i-nowi
        queue.append([i,prices[i]])
        
    while queue:
        nowi,value = queue.pop()
        answer[nowi] = len(prices)-nowi-1

    return answer
