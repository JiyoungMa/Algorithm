import sys

moving_list = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
y_dict = {'a':1, 'b':2,'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
location = sys.stdin.readline().rstrip()
loca_x = y_dict[location[0]]
loca_y = int(location[1])
count = 0
for m in moving_list:
    moving_x, moving_y = m[0], m[1]
    if loca_x+moving_x >=1 and loca_x+moving_x <=8 and loca_y+moving_y>=1 and loca_y + moving_y<=8:
        count += 1

print(count)