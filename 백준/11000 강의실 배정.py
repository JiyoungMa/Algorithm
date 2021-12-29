import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
start_times = []
end_times = []

for _ in range(n):
    s, t = map(int,input().rstrip().split())
    heapq.heappush(start_times, s)
    heapq.heappush(end_times,t)

result = 1

heapq.heappop(start_times)

while start_times:
    now_start = heapq.heappop(start_times)
    now_end = heapq.heappop(end_times)
    if now_start < now_end:
        result += 1
        heapq.heappush(end_times,now_end)

print(result)
