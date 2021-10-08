import math
def solution(n,a,b):
    answer = 1
    divide = 2
    
    while True:
        if math.ceil(a/divide) == math.ceil(b/divide):
            return answer
        else:
            answer +=1
            divide *= 2
    return answer
