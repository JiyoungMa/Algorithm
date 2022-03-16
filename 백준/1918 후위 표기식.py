import sys
from collections import deque

input = sys.stdin.readline

input_str = input().rstrip()

def getPostfix(now_str):
    stack = deque([])

    now = []

    for i in range(len(now_str)):
        if now_str[i] == "(":
            stack.append([len(now),"("])
        elif now_str[i] == ")":
            start = stack.pop()[0]
            result = getPostfix(now[start:])
            now = now[:start]
            now.append(result)
        else:
            now.append(now_str[i])

    now_second = []

    i = 0
    while i < len(now):
        if now[i] == "*" or now[i] == "/":
            temp = [now_second.pop(), now[i+1],now[i]]
            now_second.append(''.join(temp))
            i += 2
        else:
            now_second.append(now[i])
            i+=1

    now_final = []
    i = 0
    while i < len(now_second):
        if now_second[i] == "+" or now_second[i] == "-":
            temp = [now_final.pop(),now_second[i+1],now_second[i]]
            now_final.append(''.join(temp))
            i += 2
        else:
            now_final.append(now_second[i])
            i += 1

    return ''.join(now_final)

print(getPostfix(input_str))
