import sys
from itertools import combinations

n,k = map(int,sys.stdin.readline().rstrip().split(' '))
groups = list(map(int,sys.stdin.readline().rstrip().split(' ')))

list_c = list(combinations(range(n), k-1))

result = 0
for lists in list_c:
    results = []
    prev_index = 0
    for i in lists:
        results.append(sum(groups[prev_index:i]))
        prev_index = i

    results.append(sum(groups[prev_index:]))

    if min(results) > result:
        result = min(results)
print(result)