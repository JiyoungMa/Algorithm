def get_binary(n):
    answer = []
    now = 2
    
    while n>0:
        answer.append(n%now)
        n = n//now
        
    answer.reverse()
    return answer

def get_deci(binary_arr):
    now = 1
    answer = 0

    for i in range(len(binary_arr)-1,-1,-1):
        answer += now * binary_arr[i]
        now *= 2

    return answer

def solution(numbers):
    answer = []
    
    for i in numbers:
        if i == 0:
            answer.append(1)
            continue
        binary_arr = get_binary(i)

        if len(binary_arr) == binary_arr.count(1):
            binary_arr = [1,0] + binary_arr[1:]
        else:
            for i in range(len(binary_arr)-1,-1,-1):
                if binary_arr[i] == 0:
                    binary_arr[i] = 1
                    if i+1<len(binary_arr) and binary_arr[i+1]==1:
                        binary_arr[i+1] = 0
                    break
        answer.append(get_deci(binary_arr))
        
    return answer
