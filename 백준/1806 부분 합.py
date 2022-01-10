import sys

input = sys.stdin.readline

n,s = map(int,input().rstrip().split())
numbers = list(map(int,input().rstrip().split()))
prefix_sum = [0 for _ in range(n+1)]

for i in range(n):
    prefix_sum[i+1] = numbers[i]+prefix_sum[i]

start = 0
end = 0

answer = n+1
check = False

while end<=n:
    if prefix_sum[end] - prefix_sum[start] >= s:
        if answer > end - start:
            answer = end - start
            check = True
        start += 1

    else:
        if end == n:
            break
        else:
            end += 1

if check==False:
    answer = 0

print(answer)
