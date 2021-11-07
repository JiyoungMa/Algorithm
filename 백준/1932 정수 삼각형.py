import sys

n = int(sys.stdin.readline().rstrip())

numbers = []

for _ in range(n):
    numbers.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

dp =[[0 for _ in range(i)] for i in range(1,n+1,1)]

dp[0][0] = numbers[0][0]

for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + numbers[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + numbers[i+1][j+1])

print(max(dp[n-1]))
