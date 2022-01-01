import sys

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

numbers = list(map(int,input().rstrip().split()))

minus_list = [0] * (n-1)

for i in range(len(numbers)-1):
    minus_list[i] = numbers[i+1] - numbers[i]

minus_list.sort(reverse=True)
temp = minus_list[k-1:]

result = sum(temp)
print(result)
