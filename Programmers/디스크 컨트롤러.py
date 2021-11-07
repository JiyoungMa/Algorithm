def solution(jobs):
    answer = 0
    jobs.sort()
    count = len(jobs)
    
    now_time = 0
    
    while jobs:
        if jobs[0][0] >= now_time:
            now_time = jobs[0][0]
            answer += jobs[0][1]
            now_time += jobs[0][1]
            del(jobs[0])
        else:
            possible = [j for j in range(len(jobs)) if jobs[j][0] < now_time]

            now_j = -1
            minimum = int(1e9)

            for j in possible:
                if jobs[j][1]<minimum:
                    minimum = jobs[j][1]
                    now_j = j

            answer += now_time - jobs[now_j][0] + jobs[now_j][1]
            now_time += jobs[now_j][1]
            del(jobs[now_j])

    return answer // count
