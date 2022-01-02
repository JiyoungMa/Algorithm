import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
nowy, nowx, nowd = map(int,input().rstrip().split())

maps = [0] * n

for i in range(n):
    maps[i] = list(map(int,input().rstrip().split()))

visitied = [[False for _ in range(m)] for _ in range(n)]

moves = [(-1,0), (0,1), (1,0), (0,-1)]

result = 1

while True:
    visitied[nowy][nowx] = True
    check = False

    for _ in range(4):
        nowd = (nowd+3)%4

        dy = nowy + moves[nowd][0]
        dx = nowx + moves[nowd][1]

        if dy<0 or dy>=n or dx<0 or dx>=m:
            continue

        if visitied[dy][dx] == False and maps[dy][dx] == 0:
            nowy, nowx = dy, dx
            check = True
            result += 1
            break

    if check == False:
        dy = nowy - moves[nowd][0]
        dx = nowx - moves[nowd][1]

        if maps[dy][dx] == 1:
            break
        else:
            nowy,nowx = dy,dx

print(result)
