def solution(n, k, cmd):
    answer = ''
    available = [True] * n
    up = [i for i in range(-1,n-1,1)]
    up[0] = 0
    down = [i for i in range(1,n+1,1)]
    down[-1] = n-1
    delete = []
    
    move = 0
    
    for cm in cmd:
        if len(cm)>1:
            command, index = cm.split()
            index = int(index)
            
            if command == "U":
                move -= index
            else:
                move += index
        else:
            if move>0:
                while move>0:
                    move -= 1
                    k = down[k]
            elif move<0:
                while move<0:
                    move += 1
                    k = up[k]
            
            if cm == "C":
                delete.append(k)
                available[k] = False
                down[up[k]] = down[k]
                if k != down[k]:
                    k = down[k]
                    up[k] = up[up[k]]
                else:
                    k = up[k]
                    down[k] = k
            else:
                back = delete.pop()
                available[back] = True
                if up[back] != back:
                    down[up[back]] = back
                if down[back] != back:
                    up[down[back]] = back
                
    for i in available:
        if i == True:
            answer += "O"
        else:
            answer += "X"
    return answer
