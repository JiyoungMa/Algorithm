import heapq
def solution(genres, plays):
    answer = []
    genre_array = dict()
    genre_total = []
    for i in range(len(genres)):
        if genres[i] not in genre_array:
            genre_array[genres[i]] = []
        heapq.heappush(genre_array[genres[i]], (-plays[i], i))

            
    for g in genre_array:
        total = 0
        for p,i in genre_array[g]:
            total += p
        heapq.heappush(genre_total,(total,g))
        
    while genre_total:
        total, now_genre = heapq.heappop(genre_total)
        
        for _ in range(2):
            if genre_array[now_genre]:
                p,i = heapq.heappop(genre_array[now_genre])
                answer.append(i)
            
    return answer
