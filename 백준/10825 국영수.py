import sys

n = int(sys.stdin.readline().rstrip())

lists = []
for _ in range(n):
    lists.append(list(sys.stdin.readline().rstrip().split(' ')))

lists.sort(key = lambda x : (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))
for l in lists:
    print(l[0])
