from itertools import permutations
def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    numbers = [i for i in range(n)]
    ways = list(permutations(numbers,n))

    for way in ways:
        result = 0
        now_power = k

        for i in way:
            min_power, power = dungeons[i]
            if min_power <= now_power:
                now_power -= power
                result += 1

        if result > answer:
            answer = result
    return answer
