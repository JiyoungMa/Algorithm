import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp = [0 for _ in range(n)]

numbers.reverse()

dp[0] = 1
maximum = 0

for i in range(1,n,1):
    if numbers[i-1]>numbers[i]:
        for j in range(i-1,-1,-1):
            if numbers[j] < numbers[i]:
                dp[i] = dp[j]+1
                break

        if j == 0:
            dp[i] = 1
    else:
        dp[i] = maximum + 1

    if maximum < dp[i]:
        maximum = dp[i]

print(n - maximum)
        
