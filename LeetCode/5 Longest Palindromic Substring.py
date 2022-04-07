def longestPalindrome(s):
    answer = []

    for mid in range(len(s)):
        #짝수개
        start , end = mid, mid

        while True:
            if start-1 >= 0 and end + 1 < len(s) and s[start-1] == s[end+1]:
                start -= 1
                end += 1
            else:
                break
        
        nowLength = end - start + 1
        if len(answer) < nowLength:
            answer = s[start:end+1]

        #홀수개

        if mid + 1 < len(s) and s[mid] == s[mid+1]:
            start = mid
            end = mid + 1
        else:
            continue

        while True:
            if start-1 >= 0 and end + 1 < len(s) and s[start-1] == s[end+1]:
                start -= 1
                end += 1
            else:
                break
        
        nowLength = end - start + 1
        if len(answer) < nowLength:
            answer = s[start:end+1]

    return ''.join(answer)
