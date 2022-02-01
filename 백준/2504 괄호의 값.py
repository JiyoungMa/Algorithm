import sys
from collections import deque

input = sys.stdin.readline

raw_input = list(input().rstrip())
inputs = []
front_num = ""

for i in raw_input:
    if i == "(" or i == "[" or i == "]" or i==")":
        if front_num != "":
            inputs.append(int(front_num))
            front_num = ""
        inputs.append(i)
    else:
        front_num += i

result = 0
queue = deque([])
check = True

for i in inputs:
    now_result = 1
    if i == ")" or i == "]":
        if len(queue) == 0:
            check = False
            break

        now = queue.pop()
        if now != "(" and now != "[":
            now_result = now
            if len(queue) == 0:
                check = False
                break
            now = queue.pop()

        if i == ")" and now == "(":
            now_result *= 2
        elif i == "]" and now == "[":
            now_result *= 3
        else:
            check = False
            break

        while queue:
            now = queue.pop()
            if now == "(" or now == "[" or now == ")" or now == "]":
                queue.append(now)
                break
            else:
                now_result += now
        
        queue.append(now_result)
    else:
        queue.append(i)

if check == False or len(queue) != 1:
    print(0)
else:
    if queue[0] == "(" or queue[0] == ")" or queue[0] == "[" or queue[0]=="]":
        print(0)
    else:
        print(queue[0])
