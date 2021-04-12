import sys

wrong = sys.stdin.readline().rstrip()
answer = sys.stdin.readline().rstrip()

j = -1

nanswer = [-1 for _ in range(len(answer))]

for i in range(len(answer)):
    if answer[i] in wrong:
        result = []
        index = wrong.find(answer[i])
        while(index != -1):
            result.append(index)

            index = wrong.find(answer[i],index+1)

        for a in result:
            if a>j:
                nanswer[i] = a
                j = a
                break


print(nanswer)