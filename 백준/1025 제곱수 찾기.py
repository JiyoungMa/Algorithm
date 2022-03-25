import sys
import math

input = sys.stdin.readline

n, m = map(int,input().rstrip().split(' '))

input_list = []

answer = -1

for _ in range(n):
    input_list.append(list(input().rstrip()))

for now_range_y in range(-n,n,1):
    for now_range_x in range(-m,m,1):

        for y in range(n):
            for x in range(m):
                now_str = ""
                if now_range_x == 0 and now_range_y == 0:
                    now_str = input_list[y][x]
                    now_int = int(now_str)
                    if math.sqrt(now_int).is_integer():
                        if answer < now_int:
                            answer = now_int
                else:
                    nowy,nowx = y,x
                    while nowy<n and nowx<m and nowy>=0 and nowx>=0:
                        now_str += input_list[nowy][nowx]
                        nowy += now_range_y
                        nowx += now_range_x

                        if now_str == '':
                            continue

                        now_int = int(now_str)
                        if math.sqrt(now_int).is_integer():
                            if answer < now_int:
                                answer = now_int

print(answer)
