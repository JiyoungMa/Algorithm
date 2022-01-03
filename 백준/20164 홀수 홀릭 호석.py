import sys
input = sys.stdin.readline

n = input().rstrip()

def solution(n,count):
    minimum = 1e9
    maximum = -1
    for i in n:
        if int(i)%2 == 1:
            count += 1
    if len(n) == 1:
        return count, count
    elif len(n) == 2:
        return solution(str(int(n[0]) + int(n[1])), count)
    else:
        for a in range(1,len(n)-1):
            for b in range(a+1,len(n)):
                temp_n = str(int(n[0:a]) + int(n[a:b]) + int(n[b:]))
                temp_result_min, temp_result_max = solution(temp_n,count)
                if minimum > temp_result_min:
                    minimum = temp_result_min
                if maximum < temp_result_max:
                    maximum = temp_result_max
    return minimum, maximum

count = 0

minimum, maximum = solution(n,count)
print(minimum,maximum)
