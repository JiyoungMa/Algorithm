import sys
input = sys.stdin.readline

h,w = map(int,input().rstrip().split())

left = [0] * w
right = [0] * w

numbers = list(map(int,input().rstrip().split()))

left[0] = numbers[0]

for i in range(1,w):
    if left[i-1] < numbers[i]:
        left[i] = numbers[i]
    else:
        left[i] = left[i-1]

right[-1] = numbers[-1]
for i in range(w-1,0,-1):
    if right[i] < numbers[i-1]:
        right[i-1] = numbers[i-1]
    else:
        right[i-1] = right[i]

result = 0

for i in range(w):
    result += min(left[i],right[i]) - numbers[i]

print(result)
