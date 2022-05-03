from collections import deque
import heapq

def getRoot(links):
    checkConnection = [False] * len(links)
    
    for i in range(len(links)):
        left, right = links[i]
        
        if left != -1 :
            checkConnection[left] = True
        
        if right != -1 :
            checkConnection[right] = True
            
    return [i for i in range(len(links)) if checkConnection[i] == False][0]

def getArrayDict(num, links, root):
    queue = deque([[1, root]])

    arrayDict = dict()

    while queue:
        nowArray, nowNode = queue.popleft()
        arrayDict[nowArray] = num[nowNode]

        left, right = links[nowNode]

        if left != -1:
            queue.append([nowArray*2, left])

        if right != -1:
            queue.append([nowArray*2 + 1, right])

    arrayKeys = list(arrayDict.keys())
    arrayKeys.sort(reverse=True)

    for nowIndex in arrayKeys:
        if nowIndex == 1:
            break

        arrayDict[nowIndex//2] = arrayDict[nowIndex//2] + arrayDict[nowIndex]

    return arrayDict

def sliceGraph(k, arrayDict):
    heap = []
    heapq.heappush(heap,[-arrayDict[1],1])
    cut = 0

    while heap:
        nowValue, nowIndex = heapq.heappop(heap)
        nowValue = -nowValue
        if nowIndex != 1:
            nextIndex = nowIndex//2
            while nextIndex > 0:
                arrayDict[nextIndex] = arrayDict[nextIndex] - nowValue
                nextIndex = nextIndex//2
        if (nowIndex*2 not in arrayDict and nowIndex*2+1 not in arrayDict):
            continue

        cut += 1

        if nowIndex*2 in arrayDict:
            heapq.heappush(heap,(-arrayDict[nowIndex*2], nowIndex*2))
        if nowIndex*2+1 in arrayDict:
            heapq.heappush(heap,(-arrayDict[nowIndex*2+1], nowIndex*2+1))

        if cut == k:
            break

    return max(list(arrayDict.values()))

def solution(k, num, links):
    answer = 0
    
    arrayDict = getArrayDict(num, links, getRoot(links))

    return sliceGraph(k, arrayDict)

k = 1
num = [6, 9, 7, 5]
links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
print(solution(		4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
