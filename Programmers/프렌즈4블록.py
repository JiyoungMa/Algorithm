def check_erase(m,n,board):
    result = []
    move = [(1,0),(0,1),(1,1)]
    
    for y in range(m):
        for x in range(n):
            
            if board[y][x] == 0:
                continue
                
            check = True
            
            for my,mx in move:
                dy = y+my
                dx = x+mx
                
                if dy>=m or dx>=n:
                    check = False
                    break
                    
                if board[y][x] != board[dy][dx]:
                    check = False
                    break
        
            if check == True:
                result.append((y,x))
                
    return result
            
def erase_board(m,n,board,erase_arr):
    move = [(0,0),(1,0),(0,1),(1,1)]
    count = 0
    
    for y,x in erase_arr:
        for my,mx in move:
            dy = y+my
            dx = x+mx
            
            if board[dy][dx] != 0:
                count += 1
                board[dy][dx] = 0
                
    return count
            
def rearrange_board(m,n,board):
    new_board = [[] for _ in range(n)]
    
    for x in range(n):
        for y in range(m-1,-1,-1):
            if board[y][x] != 0:
                new_board[x].append(board[y][x])

    board = [[0 for _ in range(n)] for _ in range(m)]

    for y in range(n):
        for x in range(len(new_board[y])):
            board[m-x-1][y] = new_board[y][x]

    return board


def solution(m, n, board):
    answer = 0

    board = list(map(list,board))
    
    while True:
        erase_arr = check_erase(m,n,board)
        if len(erase_arr) == 0:
            break
        answer += erase_board(m,n,board,erase_arr)
        board = rearrange_board(m,n,board)
    return answer
