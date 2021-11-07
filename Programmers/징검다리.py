def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    cleared = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    while start <= end:
        cleared = 0
        mid = (start + end)//2
        dif = 0
        for i in range (len(rocks)-1):
            if(rocks[i+1]-rocks[i] + dif <mid):
                dif += rocks[i+1]-rocks[i]
                cleared += 1
            else:
                dif = 0

        if(cleared<=n):
            answer = mid
            start = mid+1
        elif(cleared>n):
            end = mid-1

    return answer
