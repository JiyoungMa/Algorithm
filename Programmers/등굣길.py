def solution(m, n, puddles):
    routes = []
    for i in range(n):
        routes.append([0]*m)
    for i in puddles:
        routes[i[1]-1][i[0]-1] = -1

    routes[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            if routes[y][x] == -1:
                continue
                
            if y-1 >=0 and routes[y-1][x] != -1:
                routes[y][x] += routes[y-1][x]
            
            if x-1>=0 and routes[y][x-1] != -1:
                routes[y][x] += routes[y][x-1]
        
    answer = routes[n-1][m-1]
    return answer %1000000007
