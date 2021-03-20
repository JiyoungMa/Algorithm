import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split(' '))
    numbers = [a%10]
    now = a%10

    while(True):
        now = now*a%10
        if now == 0:
            print(0)
            break
        elif now in numbers:
            print(numbers[b%len(numbers)-1])
            break

        numbers.append(now)