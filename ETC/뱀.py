import sys

n = int(sys.stdin.readline().rstrip())
map_list = []

for i in range(n):
    map_list.append([0 for i in range(n)])

num_apple = int(sys.stdin.readline().rstrip())

apple = []

for i in range(num_apple):
    apple.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

num_move = int(sys.stdin.readline().rstrip())
move = []

for i in range(num_move):
    move.append(list(int,sys.stdin.readline().rstrip().split(' ')))
    move[i][0] = int(move[i][0])

#북,동,남,서 순서로 바라보는 것
heading_L = {}
heading_R = {}