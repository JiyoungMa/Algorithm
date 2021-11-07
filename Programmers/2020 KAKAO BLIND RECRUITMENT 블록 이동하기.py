import heapq
def solution(board):
    answer = 0

    n = len(board)
    visitied = [[0 for _ in range(n)] for _ in range(n)]

    visits = []

    queue = []

    heapq.heappush(queue,(1,0,0,0,1))
    visitied[0][0] = 1
    visitied[0][1] = 1

    while queue:
        v, nowy1, nowx1, nowy2, nowx2 = heapq.heappop(queue)

        if nowy1 == 9 and nowx1 == 7 and nowy2 == 9 and nowx2==8:
            print("HERE")
        if [nowy1,nowx1,nowy2,nowx2] in visits:
            continue
        else:
            visits.append([nowy1,nowx1,nowy2,nowx2])

        if visitied[n-1][n-1] != 0:
            break
        if nowy1 == nowy2:

            if nowx1 -1 >=0 and board[nowy1][nowx1-1] == 0:
                visitied[nowy1][nowx1-1] = v + 1
                heapq.heappush(queue,(v+1,nowy1,nowx1-1, nowy2, nowx1))

            if nowx2+1 <n and board[nowy1][nowx2+1] == 0:
                visitied[nowy1][nowx2+1] = v+1
                heapq.heappush(queue,(v+1,nowy1,nowx2, nowy2, nowx2+1))

            if nowy1-1>=0 and board[nowy1-1][nowx1] == 0 and board[nowy1-1][nowx2] == 0:
                visitied[nowy1-1][nowx2] = v+1
                visitied[nowy1-1][nowx1] = v+1
                heapq.heappush(queue,(v+1, nowy1-1, nowx1, nowy2-1, nowx2))
                heapq.heappush(queue,(v+1,nowy1-1,nowx1,nowy1,nowx1))
                heapq.heappush(queue,(v+1,nowy1-1, nowx2, nowy2, nowx2))

            if nowy1+1<n and board[nowy1+1][nowx1] == 0 and board[nowy1+1][nowx2] == 0:
                visitied[nowy1+1][nowx2] = v+1
                visitied[nowy1+1][nowx1] = v+1
                heapq.heappush(queue,(v+1,nowy1+1, nowx1, nowy2+1, nowx2))
                heapq.heappush(queue,(v+1,nowy1,nowx1, nowy1+1,nowx1))
                heapq.heappush(queue,(v+1,nowy2,nowx2, nowy2+1,nowx2))

        if nowx1==nowx2:
            if nowy1-1>=0 and board[nowy1-1][nowx1] == 0:
                visitied[nowy1-1][nowx1] = v+1
                heapq.heappush(queue,(v+1,nowy1-1,nowx1,nowy1, nowx2))

            if nowy2+1<n and board[nowy2+1][nowx2] == 0:
                visitied[nowy2+1][nowx2] = v+1
                heapq.heappush(queue,(v+1,nowy2, nowx1, nowy2+1,nowx2))

            if nowx1-1>=0 and board[nowy1][nowx1-1] == 0 and board[nowy2][nowx1-1] == 0:
                visitied[nowy1][nowx1-1] = v+1
                visitied[nowy2][nowx1-1] = v+1
                heapq.heappush(queue,(v+1,nowy1,nowx1-1, nowy2, nowx1-1))
                heapq.heappush(queue,(v+1,nowy2,nowx1-1, nowy2, nowx2))
                heapq.heappush(queue,(v+1,nowy1,nowx1-1, nowy1,nowx1))

            if nowx1+1<n and board[nowy1][nowx1+1] == 0 and board[nowy2][nowx1+1] == 0:
                visitied[nowy1][nowx1+1] = v+1
                visitied[nowy2][nowx1+1] = v+1
                heapq.heappush(queue,(v+1, nowy1,nowx1+1, nowy2, nowx2+1))
                heapq.heappush(queue,(v+1, nowy2,nowx2, nowy2, nowx2+1))
                heapq.heappush(queue,(v+1, nowy1,nowx1, nowy1, nowx1+1))

    return visitied[n-1][n-1]-1
