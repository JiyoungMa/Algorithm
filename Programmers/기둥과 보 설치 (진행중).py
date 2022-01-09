import copy

def dfs(board,nowy,nowx,visitied):
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    visitied[nowy][nowx] = True

    for my,mx in move:
        dy = my + nowy
        dx = mx + nowx

        if dy<0 or dy >= len(board) or dx<0 or dx>= len(board):
            continue
        
        if board[dy][dx] == 1 and visitied[dy][dx] == False:
            if my == 0 and dx%2==1:
                if (0<=dy-1<len(board) and 0<=dx-1 and board[dy-1][dx-1] == 1) or (0<=dy-1<len(board) and dx+1<len(board) and board[dy-1][dx+1] == 1):
                    pass
                elif dx-2>=0 and board[dy][dx-2] == 1 and dx+2<len(board) and board[dy][dx+2] == 1:
                    pass
                else:
                    return False
            result = dfs(board, dy,dx,visitied)
            if result == False:
                return False

    return True


def check(board):
    visitied = [[False for _ in range(len(board))] for _ in range(len(board))]

    for startx in range(len(board)):
        if board[0][startx] == 1 and visitied[0][startx] == False:
            result = dfs(board,0,startx, visitied)
            if result == False:
                return False


    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 1 and visitied[y][x] == False:
                return False

    return True


def solution(n, build_frame):
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    answer = []
    board = [[0 for _ in range(n*2+1)] for _ in range(n*2+1)]

    for x,y,a,b in build_frame:
        y,x = y*2, x*2
        if b == 0:
            if a == 0:
                temp_board = copy.deepcopy(board)

                temp_board[y+1][x] = 0

                for i in range(3):
                    if i == 1:
                        continue

                    checks = False

                    for my,mx in move:
                        dy = y+my+i
                        dx = x+mx

                        if dy<0 or dy >= len(temp_board) or dx<0 or dx>= len(temp_board):
                            continue

                        if temp_board[dy][dx] == 1:
                            checks = True
                            break

                    if checks == False:
                        temp_board[y+i][x] = 0

                result = check(temp_board)
                if result == True:
                    board = temp_board
                    answer.remove([x//2,y//2,0])
            
            elif a == 1:
                temp_board = copy.deepcopy(board)
                temp_board[y][x+1] = 0
                for i in range(3):
                    if i == 1:
                        continue

                    checks = False

                    for my,mx in move:
                        dy = y+my
                        dx = x+mx+i

                        if dy<0 or dy >= len(temp_board) or dx<0 or dx>= len(temp_board):
                            continue

                        if temp_board[dy][dx] == 1:
                            checks = True
                            break

                    if checks == False:
                        temp_board[y][x+i] = 0

                result = check(temp_board)
                if result == True:
                    board = temp_board
                    answer.remove([x//2,y//2,1])
        if b == 1:
            if a == 0:
                temp_board = copy.deepcopy(board)
                
                for i in range(3):
                    temp_board[y+i][x] = 1

                result = check(temp_board)
                
                if result == True:
                    board = temp_board
                    answer.append([x//2,y//2,0])

            elif a == 1:
                temp_board = copy.deepcopy(board)
                
                for i in range(3):
                    temp_board[y][x+i] = 1

                result = check(temp_board)
                
                if result == True:
                    board = temp_board
                    answer.append([x//2,y//2,1])

    answer = sorted(answer,key = lambda x : x[0])
    return answer
