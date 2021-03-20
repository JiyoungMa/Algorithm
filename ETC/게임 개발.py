import sys

map_x, map_y = map(int, sys.stdin.readline().rstrip().split(' '))
loca_x, loca_y, head = map(int, sys.stdin.readline().rstrip().split(' '))

moving_head= {0:3, 3:2, 2:1, 1:0}
moving_dict = {0:[-1,0], 1:[0,-1], 2:[1,0], 3:[0,1]}
moving_back = {0:[0,1], 1:[-1,0], 2:[0,1], 3:[1,0]}

map_list = []
extra =[0]*(map_y+2)
map_list.append(extra)
for i in range(map_y):
    l = [0]
    l.extend(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    l.append(0)
    map_list.append(l)

map_list.append(extra)

map_list[loca_y][loca_x] = 2
while(True):
    moving_x, moving_y = moving_dict[head][0], moving_dict[head][1]
    around=map_list[loca_y-1][loca_x-1 : loca_x+2]
    around.extend(map_list[loca_y][loca_x-1 : loca_x+2])
    around.extend(map_list[loca_y+1][loca_x-1 : loca_x+2])

    if around.count(1) == 0:
        if map_list[moving_back[head][1]+loca_y][moving_back[head][0]+loca_x] == 0:
            break
        else:
            loca_y += moving_back[head][1]
            loca_x += moving_back[head][0]
    elif map_list[moving_y+loca_y][moving_x+loca_x] == 1:
        loca_y += moving_y
        loca_x += moving_x
        head = moving_head[head]
        map_list[loca_y][loca_x] = 2

    elif map_list[moving_y+loca_y][moving_x+loca_x] == 2 or map_list[moving_y+loca_y][moving_x+loca_x] == 0:
        head = moving_head[head]

print(map_list[1].count(2)-1)