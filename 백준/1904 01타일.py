import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * 1000003

dp[0] = 1
for i in range(n):
    dp[i+1] = (dp[i+1] + dp[i])%15746
    dp[i+2] = (dp[i+2]+dp[i])%15746

print(dp[n])
