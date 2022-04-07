def lengthOfLongestSubstring(s):
    answerList = []
    if len(s)== 0:
        return 0
    start = 0
    end = 0
    nowChar = [s[start]]

    while end+1 <len(s):
        if s[end+1] not in nowChar:
            end += 1
            nowChar.append(s[end])
        else:
            answerList.append(''.join(s[start:end+1]))
            indexs = nowChar.index(s[end+1])
            end = start + indexs + 1
            start = end
            nowChar = [s[start]]

    answerList.append(''.join(s[start:end+1]))

    answer = max(answerList, key = len)

    return len(answer)

