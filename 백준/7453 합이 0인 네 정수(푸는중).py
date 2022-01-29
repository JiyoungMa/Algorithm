import sys
from itertools import product

input = sys.stdin.readline

n = int(input().rstrip())

lists = []*4
items = [[i for i in range(n)] for _ in range(4)]

for _ in range(n):
    numbers = list(map(int,input().rstrip().split()))
    for i in range(4):
        lists[i].append(numbers[i])

products = list(product(*items))

result = 0

for p in products:
    now_result = 0
    for i in range(4):
        now_result += lists[i][p[i]]

    if now_result == 0:
        result += 1

print(now_result)
