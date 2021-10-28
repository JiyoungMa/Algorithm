def solution(number, k):
    answer = ''
    want_length = len(number) - k
    number = list(number)
    start = 0
    
    while want_length>0:
        maximum = '-1'
        max_index = -1
        
        for i in range(start,len(number)-want_length+1):
            if number[i] > maximum:
                max_index = i
                maximum = number[i]
                if maximum == '9':
                    break
                
        answer += maximum
        start = max_index + 1
        want_length -= 1
    return answer
