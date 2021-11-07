def solution(n, words):
    answer = []
    a = -1
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            a = i
            break
        
        if len(words[i]) == 1:
            a = i
            break
            
        if words[i] in words[:i]:
            a = i
            break
            
    print(a)
    if a == -1:
        answer = [0,0]
    else:
        if (a+1)%n == 0:
            answer.append(n)
        else:
            answer.append((a+1)%n)
            
        answer.append(a//n+1)

    return answer
