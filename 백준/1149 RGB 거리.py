import sys

n = int(sys.stdin.readline().rstrip())

values = []
for _ in range(n):
    values.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

dp = [[0,0,0] for _ in range(n)]

dp[0] = values[0]

for i in range(1,n,1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + values[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + values[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + values[i][2]

print(min(dp[n-1]))