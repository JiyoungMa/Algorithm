import sys

input = sys.stdin.readline

n = int(input().rstrip())

graph = []
answerBlue = 0
answerWhite = 0

for _ in range(n):
    graph.append(list(map(int,input().rstrip().split(' '))))

nowLength = n

while nowLength >= 1:
    for starty in range(0,n,nowLength):
        for startx in range(0,n,nowLength):
            check = True
            color = -1
            for y in range(starty, starty+nowLength,1):
                for x in range(startx, startx+nowLength, 1):
                    if graph[y][x] == -1:
                        check = False
                        break
                    
                    if color == 1 and graph[y][x] != 1:
                        check = False
                        break
                    elif color == 0 and graph[y][x] != 0:
                        check = False
                        break
                    elif color == -1:
                        color = graph[y][x]
                if check == False:
                    break
            if check == True:
                if color == 1:
                    answerBlue += 1
                else:
                    answerWhite += 1
                for y in range(starty, starty+nowLength,1):
                    for x in range(startx, startx+nowLength, 1):
                        graph[y][x] = -1
    nowLength = nowLength//2
print(answerWhite)
print(answerBlue)
