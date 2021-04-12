import sys

n,m = map(int,sys.stdin.readline().rstrip().split(' '))
dp = [-1 for i in range(10001)]
coins = []
for i in range(n):
    c = int(sys.stdin.readline().rstrip())
    coins.append(c)
    dp[c] = 1

for i in range(m+1):
    result = []
    for j in coins:
        if dp[i-j] != -1:
            result.append(dp[i-j]+1)

    if len(result) != 0:
        dp[i] = min(result)

print(dp[m])