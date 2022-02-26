import sys
def binary_search_while(array,target, start, end):
    while start<= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else :
            start = mid +1

    return None

n = int(input())
parts = list(map(int,sys.stdin.readline().rstrip().split()))

m = int(input())
finding = list(map(int,sys.stdin.readline().rstrip().split()))

parts.sort()


for i in finding:
    index = binary_search_while(parts,i,0,n-1)
    if index != None:
        print("1", end = ' ')
    else :
        print("0", end = ' ')
