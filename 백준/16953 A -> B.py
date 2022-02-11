import sys

a,b = map(int,sys.stdin.readline().rstrip().split(' '))

count = 1
while(a != b):
    if(b<a):
        count = -1
        break
    while(b%2 == 0 and a != b):
        b = b//2
        count += 1
    if a==b:
        break
    elif b%10 == 1:
        b = b//10
        count += 1
    else:
        count = -1
        break

print(count)
