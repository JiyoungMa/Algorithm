import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().rstrip().split(' '))
    n = int(sys.stdin.readline().rstrip())

    count = 0
    for _ in range(n):
        ox, oy, r = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        if (ox-x1)**2 + (oy-y1)**2 < r**2 and (ox-x2)**2 + (oy-y2)**2 < r**2:
            continue
        elif (ox-x1)**2 + (oy-y1)**2 < r**2:
            count+=1
        elif (ox-x2)**2 + (oy-y2)**2 < r**2:
            count += 1

    print(count)