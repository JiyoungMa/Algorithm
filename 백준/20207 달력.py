import sys

input = sys.stdin.readline

n = int(input().rstrip())

years = [0] * 366

for _ in range(n):
    start, end = map(int,input().rstrip().split())

    for i in range(start,end+1):
        years[i] += 1

answer = 0

start = -1
for i in range(1,len(years)):
    if start == -1 and years[i] != 0:
        start = i
    elif start != -1 and years[i] == 0:
        height = max(years[start:i])
        answer += (i - start) * height
        start = -1

if start != -1 :
    height = max(years[start:])
    answer += (len(years)-start)*height

print(answer)
