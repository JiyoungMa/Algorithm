import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp = [0 for i in range(n)]
dp[0] = numbers[0]
dp[1] = max(numbers[0],numbers[1])

for i in range(2,n,1):
    dp[i] = max(dp[i-2]+numbers[i], dp[i-1])

print(dp[n-1])