import sys
import math

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split(' '))

    result = (x1-x2)**2 + (y1-y2)**2
    if x1==x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    
    elif (r1-r2)**2 <result < (r1+r2)**2:
        print(2)
    
    elif result == (r1+r2)**2:
        print(1)

    elif math.sqrt(result) + r1 == r2:
        print(1)

    elif math.sqrt(result) + r2 == r1:
        print(1)

    else:
        print(0)