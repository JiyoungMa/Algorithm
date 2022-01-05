import sys
input = sys.stdin.readline

n,c = map(int,input().rstrip().split())
m = int(input().rstrip())

plan = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,d = map(int,input().rstrip().split())
    plan[a].append((b,d))


now_result = 0
now_weight = 0
now_visit = dict()
now = 1

while True:
    if len(plan[now]) > 0:
        now_sorted = sorted(plan[now], key = lambda x : x[1])

        for d,w in now_sorted:
            if now_weight + w <= c:
                now_result += w
                now_weight += w
                if d in now_visit:
                    now_visit[d] += w
                else:
                    now_visit[d] = w
            elif now_weight < c:
                plus_weight = c - now_weight
                now_weight += plus_weight 
                now_result += plus_weight 
                if d in now_visit:
                    now_visit[d] += plus_weight
                else:
                    now_visit[d] = plus_weight
            else:
                break
    
    if now == n:
        break

    now += 1

    if now in now_visit:
        now_weight -= now_visit[now]
        del(now_visit[now])


print(now_result)
