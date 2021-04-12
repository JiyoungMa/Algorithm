import sys

n = int(sys.stdin.readline().rstrip())

result = dict()
result[1] = 0
result[2] = 1
result[3] = 1
result[5] = 1

def function(n):
    rresult = []
    if n in result.keys():
        return result[n]
    else:
        if n % 5== 0:
            rresult.append( function(n//5) + 1)
        if n%3 == 0:
            rresult.append(function(n//3) + 1)
        if n%2 == 0:
            rresult.append( function(n//2) + 1)
        

        rresult.append(function(n-1) + 1)

        result[n] = min(rresult)
        return result[n]

print(function(n))