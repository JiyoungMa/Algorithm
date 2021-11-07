def solution(N, number):
    answer = 0
    nums = [[] for _ in range(9)]
    nums[1].append(N)
    
    for i in range(1,9):
        for j in range(1,9-i):
            for x in nums[i]:
                if x*10 + N not in nums[i+1]:
                    nums[i+1].append(x*10+N)
                for y in nums[j]:
                    if x+y not in nums[i+j]:
                        nums[i+j].append(x+y)
                    if abs(x-y) not in nums[i+j] and abs(x-y) != 0:
                        nums[i+j].append(abs(x-y))
                    if x*y not in nums[i+j]:
                        nums[i+j].append(x*y)
                    if x//y not in nums[i+j] and x//y != 0:
                        nums[i+j].append(x//y)      
    answer = -1
    for i in range(1,9):
        if number in nums[i]:
            return i              
    return answer
