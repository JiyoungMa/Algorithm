import sys

number_list = list(sys.stdin.readline().rstrip())
number_list = list(map(int, number_list))

half = len(number_list)//2
count_l = sum(number_list[0:half])
count_r = sum(number_list[half:])

if count_l == count_r:
    print("LUCKY")
else:
    print("READY")
