import sys

n = int(sys.stdin.readline().rstrip())
moving = list(sys.stdin.readline().rstrip().split(' '))

#R,L,U,D
xy_list= [[1,0], [-1,0],[0,-1], [0,1]]
start_x = 1
start_y = 1
moving_x, moving_y = 0,0
for m in moving:
    if m == 'R':
        moving_x, moving_y = xy_list[0][0], xy_list[0][1]
    elif m == 'L':
        moving_x, moving_y = xy_list[1][0], xy_list[1][1]
    elif m == 'U':
        moving_x, moving_y = xy_list[2][0], xy_list[2][1]
    elif m == 'D':
        moving_x, moving_y = xy_list[3][0], xy_list[3][1]
    else:
        moving_x, moving_y = 0,0

    if start_x<=1 and moving_x<0:
        moving_x = 0
    elif start_x >= n and moving_x>0:
        moving_x = 0

    if start_y<=1 and moving_y<0:
        moving_y = 0
    elif start_y>=n and moving_y>0:
        moving_y = 0

    start_x += moving_x
    start_y += moving_y

print(str(start_y)+" " + str(start_x))