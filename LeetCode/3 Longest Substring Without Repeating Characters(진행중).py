from copy import deepcopy


def lengthOfLongestSubstring(s):
    countCharsTotal = dict()

    if len(s) == 0:
        return 0
    
    for nows in s:
        if nows in countCharsTotal:
            countCharsTotal[nows] += 1
        else:
            countCharsTotal[nows] = 1
            
    def getLongesStr(start,end,s,nowCharsTotal):
        answer = 1

        while start < end:
            check = True
            for i in nowCharsTotal:
                if nowCharsTotal[i] > 1:
                    check = False
                    break

            if check == True:
                return start,end,end-start+1,nowCharsTotal

            checkDiff = False

            if nowCharsTotal[s[start]]>1:
                nowCharsTotal[s[start]] -= 1
                start += 1
                checkDiff = True

            if nowCharsTotal[s[end]]>1:
                nowCharsTotal[s[end]] -= 1
                end -= 1
                checkDiff = True

            if checkDiff == False:
                nextCharsTotal1 = deepcopy(nowCharsTotal)
                nextCharsTotal1[s[start]] -= 1
                start1,end1,answer1,nextCharsTotal1 = getLongesStr(start+1,end,s,nextCharsTotal1)

                nextCharsTotal2 = deepcopy(nowCharsTotal)
                nextCharsTotal2[s[end]] -= 1
                start2,end2,answer2,nextCharsTotal2 = getLongesStr(start,end-1, s, nextCharsTotal2)

                if answer1>answer2:
                    return start1,end1,answer1, nextCharsTotal1
                else:
                    return start2, end2, answer2, nextCharsTotal2

        return start,end,end-start+1, nowCharsTotal

    answer = getLongesStr(0,len(s)-1,s,countCharsTotal)
    print(answer)
    return answer[2]
