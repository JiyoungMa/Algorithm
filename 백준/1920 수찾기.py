import sys


n = int(sys.stdin.readline().rstrip())
n_numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))
m = int(sys.stdin.readline().rstrip())
m_numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

n_numbers.sort()


def binarysearch(i):
    start = 0
    end = n-1
    while(start<=end):
        mid = (start+end)//2
        if n_numbers[mid] == i:
            return True
        elif n_numbers[mid] > i:
            end = mid-1
        elif n_numbers[mid] < i:
            start = mid +1
    return False

for i in m_numbers:
    if binarysearch(i):
        print(1)
    else:
        print(0)