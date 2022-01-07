import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    strings = input().rstrip()
    k = int(input().rstrip())

    count = [[] for _ in range(26)]

    answer_min = len(strings)
    answer_max = 0
    check = False

    for i in range(len(strings)):
        count[ord(strings[i]) - ord('a')].append(i)
        if len(count[ord(strings[i]) - ord('a')]) >= k:
            result = i - count[ord(strings[i]) - ord('a')][-k] + 1
            if result > answer_max:
                check = True
                answer_max = result
            if result < answer_min:
                check = True
                answer_min = result

    if check == False:
        print(-1)
    else:
        print(answer_min, answer_max)
