import sys

n = int(sys.stdin.readline().rstrip())

array = list(map(int,sys.stdin.readline().rstrip().split()))

array.sort()
if len(array)%2 == 0:
    print(array[len(array)//2-1])
else:
    print(array[len(array)//2])
