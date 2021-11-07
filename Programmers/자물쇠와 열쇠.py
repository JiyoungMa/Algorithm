import sys
import copy

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

def turn_right(key):
    out_key = []
    for i in range(len(key[0])):
        out_key.append([])

    for i in range(len(key)-1,-1,-1):
        for j in range(len(key[i])):
            out_key[j].append(key[i][j])

    return out_key


real_lock =[]

for i in range(len(lock)+2*len(key) - 2):
    real_lock.append([0 for j in range(len(lock[0]) + 2*len(key[0]) - 2)])

for i in range(len(lock)):
    for j in range(len(lock[0])):
        real_lock[i+len(key)-1][j+len(key[0])-1] = lock[i][j]


for i in range(4):
    for y in range(len(real_lock)-len(key)):
        for x in range(len(real_lock[0]) - len(key[0])):
            r_lock = copy.deepcopy(real_lock)
            for yy in range(len(key)):
                for xx in range(len(key[0])):
                    r_lock[yy+y][xx+x] += key[yy][xx]
            check = True
            for i in range(len(lock)):
                c = r_lock[i+len(key)-1][len(key[0])-1 : len(key[0])*2 -1]
                if c.count(1) != len(c):
                    check = False
                    break
            if check == True:
                print('true')
    key = turn_right(key)

print('false')
            
