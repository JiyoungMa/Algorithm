import sys

t= int(sys.stdin.readline().rstrip())

for _ in range(t):
    n,m = map(int,sys.stdin.readline().rstrip().split(' '))
    numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    maps = []
    for i in range(n):
        maps.append(numbers[i*m : (i+1)*(m)])
    
    dp = [[0 for _ in range(m)] for _ in range(n)]

    moving = [[1,0],[1,1],[1,-1]]

    for y in range(n):
        dp[y][0] = maps[y][0]
        
    for x in range(m):
        for y in range(n):
            for mx,my in moving:
                dx = x+mx
                dy = y+my

                if dx<0 or dx>=m or dy<0 or dy>=n:
                    continue

                dp[dy][dx] = max(dp[dy][dx], dp[y][x]+maps[dy][dx])

    maximum = 0

    for x in range(m):
        for y in range(n):
            if dp[y][x] > maximum:
                maximum = dp[y][x]

    print(maximum)