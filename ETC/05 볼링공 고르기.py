import sys
n,m = map(int,sys.stdin.readline().rstrip().rsplit(' '))
balls = list(map(int,sys.stdin.readline().rstrip().rsplit(' ')))

count = 0

for i in range(len(balls)):
    for j in range(i+1,len(balls),1):
        if(balls[i] != balls[j]):
            count += 1

print(count)