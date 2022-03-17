import sys

input = sys.stdin.readline

input_str = input().rstrip()

ord_str = [ord(i) for i in input_str]

visited = [False] * len(input_str)

def getNext(now_start, now_end):
    if visited.count(False) == 0:
        return

    if visited[now_start:now_end].count(False) == 0:
        check = False
        for i in range(now_start-1,-1,-1):
            if visited[i] == True:
                now_end = now_start
                now_start = i
                check = True
                break
        if check == False:
            now_end = now_start
            now_start = 0
        getNext(now_start, now_end)
    else:
        now_list = [ord_str[i] for i in range(now_start,now_end) if visited[i] == False]
        min_value = min(now_list)
        for i in range(now_start,now_end):
            if visited[i] == False and ord_str[i] == min_value:
                now_start = i
                break
        visited[now_start] = True
        now_str = ''.join([input_str[i] for i in range(len(visited)) if visited[i] == True])
        print(now_str)
        getNext(now_start,now_end)

getNext(0,len(visited))
