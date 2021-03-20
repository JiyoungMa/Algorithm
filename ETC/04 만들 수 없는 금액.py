import sys

coin_num = int(sys.stdin.readline().rstrip())
coin_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))

coin_list.sort()

target = 1

if coin_list[0] != 1:
    result = 1

else:
    for i in coin_list:
        if target < i:
            break
        target += i

3 2 1 1 9
1 1 2 3 9

1 1 2 9

0 1 / 2 3 / 4 9 10 11 12 13