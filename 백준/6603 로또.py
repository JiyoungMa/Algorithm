import sys

def dfs(group,start,n_list,results):
    for i in group[start]:
        next_list = n_list[:]
        next_list.append(i)
        if len(next_list) != 6:
            dfs(group,i,next_list,results)
        else:
            next_list = list(map(str,next_list))
            results.append(" ".join(next_list))
            for n in next_list:
                if n in group[i]:
                    group[i].remove(n)
                
results = []
while(True):
    numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

    if numbers == [0]:
        results.pop()
        break
    
    size = numbers[0]
    numbers = numbers[1:]
    group = [[] for i in range(51)]
    for i in range(size):
        group[numbers[i]] = [numbers[j] for j in range(i+1,size,1)]


    for i in numbers:
        dfs(group,i,[i],results)

    results.append('')

for s in results:
    print(s)