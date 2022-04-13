from copy import deepcopy
import sys
from itertools import permutations


def rotateFunc(c,r,s, arr):
    startx = r - s - 1
    starty = c - s - 1
    index = 1
    while True:
        if startx == r-1 and starty == c - 1:
            break

        temp = arr[starty][startx]

        for nowy in range(starty, c+s-index):
            arr[nowy][startx] = arr[nowy+1][startx]

        for nowx in range(startx, r+s-index):
            arr[c+s-index][nowx] = arr[c+s-index][nowx+1]

        for nowy in range(c+s-index, starty, -1):
            arr[nowy][r+s-index] = arr[nowy-1][r+s-index]

        for nowx in range(r+s-index, startx,-1):
            arr[starty][nowx] = arr[starty][nowx-1]

        arr[starty][startx+1] = temp

        startx += 1
        starty += 1
        index += 1

input = sys.stdin.readline

n,m,k = map(int, input().rstrip().split(' '))

answer = 10**5

arr = []
rotate = []
rotatearr = [i for i in range(k)]

for _ in range(n):
    arr.append(list(map(int,input().rstrip().split(' '))))


for _ in range(k):
    rotate.append(list(map(int,input().rstrip().split(' '))))

rotatePerm = list(permutations(rotatearr,k))

for nowRotate in rotatePerm:
    nowArr = deepcopy(arr)
    for rotateIndex in nowRotate:
        nowR, nowC, nowS = rotate[rotateIndex]
        rotateFunc(nowR, nowC, nowS, nowArr)
    answer = min(answer, min([sum(nowArr[i]) for i in range(n)]))

print(answer)
