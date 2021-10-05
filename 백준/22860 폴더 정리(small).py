import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

folder_dict = dict()
folder_dict['main'] = [[],[],0]

for _ in range(n+m):
    A,B,f = input().rstrip().split()
    f = int(f)
    if A not in folder_dict.keys():
        folder_dict[A] = [[],[],0]

    if f == 0:
        folder_dict[A][1].append(B)
    else:
        if B in folder_dict.keys():
            folder_dict[B][0].append(A)
            folder_dict[A][2] += 1
        else:
            folder_dict[B] = [[A],[],0]
            folder_dict[A][2] += 1

for f in folder_dict.keys():
    folder_dict[f][1] = list(set(folder_dict[f][1]))
    if f != 'main' and len(folder_dict[f][0]) == 0:
        folder_dict[f][0].append('main')

queue = deque([])

for f in folder_dict.keys():
    if folder_dict[f][2] == 0:
        queue.append(f)

while queue:
    nowf = queue.popleft()

    for nextf in folder_dict[nowf][0]:
        folder_dict[nextf][1] += folder_dict[nowf][1]
        folder_dict[nextf][2] -= 1
        if folder_dict[nextf][2] == 0:
            queue.append(nextf)

n = int(input().rstrip())

for _ in range(n):
    ask = list(input().rstrip().split('/'))
    if ask[-1] in folder_dict.keys():
        temp = folder_dict[ask[-1]][1]
        temp = set(temp)
        print(len(temp),len(folder_dict[ask[-1]][1]))
    else:
        print(0,0)
