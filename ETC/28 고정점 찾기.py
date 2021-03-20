import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

def binarysearch(start,end):
    if start > end:
        return None

    mid = (start+end)//2
    if numbers[mid] == mid:
        return mid

    elif numbers[mid] > mid :
        return binarysearch(start, mid-1)

    elif numbers[mid] < mid:
        return binarysearch(mid+1,end)

result = binarysearch(0,len(numbers)-1)
if result == None:
    print(-1)
else:
    print(result)