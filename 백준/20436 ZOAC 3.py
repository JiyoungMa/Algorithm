import sys
input = sys.stdin.readline

l,r = input().rstrip().split()

want_str = list(input().rstrip())

keyboard_list = ['qwertyuiop','asdfghjkl','zxcvbnm']
keyboard = dict()

for y in range(3):
    for x in range(len(keyboard_list[y])):
        keyboard[keyboard_list[y][x]] = (y,x)

ly,lx = keyboard[l]
ry,rx = keyboard[r]

result = 0

l_str = "qwertasdfgzxcv"

for s in want_str:
    sy,sx = keyboard[s]

    if s in l_str:
        result += 1 + abs(sy-ly) + abs(sx-lx)
        ly,lx = sy,sx
    else:
        result += 1 + abs(sy-ry) + abs(sx-rx)
        ry,rx = sy,sx

print(result)
