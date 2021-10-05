import sys
input = sys.stdin.readline

attacks = []
attack_direction = [(-1,0), (1,0), (0,-1), (0,1)]
answer = [0,0,0]

n,m = map(int, input().rstrip().split())

maps = [0] * (n*n)
shark_x, shark_y = (n+1)//2 - 1, (n+1)//2 - 1

inputs = []
for _ in range(n):
    inputs.append(list(map(int,input().rstrip().split())))

for _ in range(m):
    attacks.append(list(map(int,input().rstrip().split())))

def mapsWithNumbers(n):
    number_maps = [[0 for _ in range(n)] for _ in range(n)]
    direction = 0
    start_x = -1
    start_y = 0
    now_number = n*n-1
    now_length = n

    while now_number>0:
        if direction == 0:
            for _ in range(now_length):
                start_x += 1
                number_maps[start_y][start_x] = now_number
                now_number -= 1

        elif direction == 1:
            now_length -= 1
            for _ in range(now_length):
                start_y += 1
                number_maps[start_y][start_x] = now_number
                now_number -= 1

        elif direction == 2:
            for _ in range(now_length):
                start_x -= 1
                number_maps[start_y][start_x] = now_number
                now_number -= 1

        else:
            now_length -= 1
            for _ in range(now_length):
                start_y -= 1
                number_maps[start_y][start_x] = now_number
                now_number -= 1

        direction = (direction+1) % 4

    return number_maps

number_maps = mapsWithNumbers(n)

for y in range(n):
    for x in range(n):
        maps[number_maps[y][x]] = inputs[y][x]

i = 1
while i<len(maps):
    if maps[i] == 0 :
        del(maps[i])
    else:
        i += 1

def attackMap(d,s):
    my,mx = attack_direction[d-1]
    ny, nx = shark_y, shark_x

    for i in range(s):
        ny = my+ny
        nx = mx+nx

        if ny>=0 and ny<n and nx>=0 and nx<n:
            now = number_maps[ny][nx] - i

            if now < len(maps):
                del(maps[now])

def removeMap():
    bools = False
    remove_list = [0] * (n*n)
    now = maps[1]
    count = 0
    i = 1

    while i< len(maps):
        remove_list[i-1] = [now,count]
        if now != maps[i]:
            if count >=4:
                del(maps[i-count:i])
                del(remove_list[i-count:i])
                answer[now-1] += count
                i = i - count
                count = 0
                now = maps[i]
                bools = True
                #now,count = remove_list[i-1]
            else:
                count = 1
                now = maps[i]
                i += 1
        else:
            count += 1
            i += 1

    remove_list[i-1] = [now,count]

    if count >= 4:
        del(maps[-count:])
        remove_list = remove_list[0:len(maps)]
        answer[now-1] += count
    return remove_list, bools

def makeNewMap(remove_list):
    maps = [0]

    for i in range(1,len(remove_list)-1):
        if remove_list[i+1] != 0:
            if remove_list[i][0] != remove_list[i+1][0]:
                maps.append(remove_list[i][1])
                maps.append(remove_list[i][0])
        elif remove_list[i] != 0:
            maps.append(remove_list[i][1])
            maps.append(remove_list[i][0])
            break
            
        if len(maps) >= n*n:
            maps = maps[0:n*n]
            return maps

    if len(maps) >= n*n:
        maps = maps[0:n*n]
    return maps

for d,s in attacks:
    if len(maps) < 2:
        break
    attackMap(d,s)
    bools = True
    while bools:
        remove_list,bools = removeMap()
    maps = makeNewMap(remove_list)

result = answer[0] + 2*answer[1] + 3*answer[2]

print(result)
