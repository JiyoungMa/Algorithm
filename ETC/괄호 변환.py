def solution(p):
    p = list(p)
    perfect = []
    start_i = 0
    while(True):
        left = 0
        right = 0
        
        for i in range(start_i,len(p),1):
            if p[i] == '(':
                left += 1
            elif p[i] == ')':
                right += 1

            if left<right:
                break

        if i == len(p) -1:
            return ''.join(p)

        perfect.extend(p[start_i : i])

        left = 0
        right = 0

        for ii in range(i,len(p),1):
            if p[ii] == '(':
                left += 1
            elif p[ii] == ")":
                right += 1

            if left==right:
                ii+=1
                break
        
        wrong = p[i:ii]
        for i in range(left):
            perfect.append('(')

        for i in range(right):
            perfect.append(')')

        p = perfect[:] + p[len(perfect):]


    answer = str(perfect)
    return answer

print(solution("(()()())"))