from itertools import count
import sys
import heapq
import copy

input = sys.stdin.readline

n, m = map(int,input().rstrip().split(' '))

graph = []
cctv_location = []
count_wall = 0

for y in range(n):
    graph.append(list(map(int,input().rstrip().split(" "))))
    for x in range(m):
        if 1<=graph[y][x]<=5:
            cctv_location.append([x,y])
        elif graph[y][x] == 6:
            count_wall += 1

moves = [(0,1),(1,0),(0,-1),(-1,0)]
cctvs = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

def getCCTV(cctv_index,input_graph,result):
    answer = 0
    if cctv_index >= len(cctv_location):
        return result

    cx,cy = cctv_location[cctv_index]
    cctv_direction = input_graph[cy][cx]
    
    for m_index in cctvs[cctv_direction]:
        now_graph = copy.deepcopy(input_graph)
        temp_result = result
        for now_moves in m_index:
            nx,ny = cx,cy
            mx,my = moves[now_moves]
            dx,dy = nx+mx,ny+my
            while 0<=dx<m and 0<=dy<n:
                if now_graph[dy][dx] == 6:
                    break
                if now_graph[dy][dx] == 0:
                    now_graph[dy][dx] = '#'
                    temp_result += 1

                dy += my
                dx += mx
        answer = max(answer,getCCTV(cctv_index+1, now_graph,temp_result))
    
    return answer

print(n*m - (getCCTV(0,graph,0)+len(cctv_location)+count_wall))
