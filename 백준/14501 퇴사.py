import sys

n = int(sys.stdin.readline().rstrip())

days = []
pay = []

for i in range(n):
    d,p = map(int,sys.stdin.readline().rstrip().split(' '))
    days.append(d)
    pay.append(p)

dp = [0 for _ in range(n+1)]


for i in range(len(days)):
    time = i+days[i]
    if time<=n:
        if i !=0 :
            dp[i+days[i]] = max(dp[i]+pay[i],max(dp[0:i]) + pay[i], dp[i+days[i]])
        else:
            dp[i+days[i]] = max(dp[i]+pay[i], dp[i+days[i]])
    

print(max(dp))
