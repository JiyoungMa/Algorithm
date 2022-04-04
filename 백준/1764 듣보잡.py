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



n,m = map(int, input().split())
list1 = []
answer = []

for i in range(n):
    list1.append(sys.stdin.readline().rstrip())

list1.sort()

for i in range(m):
    name = sys.stdin.readline().rstrip()
    if binary_search_while(list1, name, 0, n-1) != None:
        answer.append(name)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
