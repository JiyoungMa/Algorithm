import sys
input = sys.stdin.readline

n = int(input().rstrip())

numbers = list(map(int,input().rstrip().split()))

numbers.sort()
start = 0
end = len(numbers)-1

answer1, answer2 = numbers[0], numbers[-1]
while start < end:
    if abs(numbers[end] + numbers[start]) < abs(answer1+answer2):
        answer1,answer2 = numbers[start], numbers[end]
    
    if abs(numbers[end] + numbers[start+1]) < abs(numbers[end-1] + numbers[start]):
        start += 1
    else:
        end -= 1

print(min(answer1,answer2), max(answer1,answer2))
