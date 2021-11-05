def solution(citations):
    answer = -1
    citations.sort(reverse=True)

    for i in range(len(citations)-1):
        if citations[i]>=i+1>=citations[i+1]:
            return i+1
        
    if citations[0] == 0:
        return 0
    return len(citations)
