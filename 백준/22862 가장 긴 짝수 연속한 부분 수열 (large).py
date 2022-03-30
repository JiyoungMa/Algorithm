import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split(' '))

numbers = []

input_list = list(map(int,input().rstrip().split(' ')))

for i in range(len(input_list)):
    if input_list[i]%2 == 0:
        numbers.append(i)

start = 0
end = 0
answer = 0

while end<len(numbers):
    if numbers[end] - numbers[start] - (end - start)<= k :
        nowResult = end - start + 1
        answer = max(answer,nowResult)
        end += 1
    else:
        start += 1

print(answer)
