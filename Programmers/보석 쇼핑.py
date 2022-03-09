def solution(gems):
    jewels = len(set(gems))
    start, end = 0,0
    answer = [0,len(gems)-1]
    jewels_dict = dict()

    jewels_dict[gems[start]] = 1

    while(start<= end and end<len(gems)):
        if len(jewels_dict.keys())==jewels:
            if answer[1]-answer[0] > end - start:
                answer = [start,end]

        if start < end and jewels_dict[gems[start]] > 1:
            jewels_dict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end<len(gems):
                if gems[end] in jewels_dict.keys():
                        jewels_dict[gems[end]] += 1
                else:
                    jewels_dict[gems[end]] = 1

    answer = [answer[0]+1, answer[1]+1]
    return answer
