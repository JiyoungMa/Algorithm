import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

input_str = input().rstrip() #(0/(0))

stack = deque([])

brackets = []

for i in range(len(input_str)):
    if input_str[i] == "(":
        stack.append(i)
    elif input_str[i] == ")":
        brackets.append([stack.pop(),i])

bracket_num = [i for i in range(len(brackets))]

answer = []

for i in range(1,len(brackets)+1):
    now_comb = list(combinations(bracket_num,i))

    for c in now_comb:
        now_remove = []
        for j in c:
            now_remove.extend(brackets[j])

        now_result = ''.join([input_str[i] for i in range(len(input_str)) if i not in now_remove])
        answer.append(now_result)

answer = list(set(answer))
answer.sort()

for s in answer:
    print(s)
