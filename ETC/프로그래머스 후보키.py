from itertools import combinations

def solution(relation):
    answer = 0
    already = []
    
    columns = [[] for _ in range(len(relation[0]))]
    
    for r in relation:
        for i in range(len(r)):
            columns[i].append(r[i])
            
    for c in range(len(columns)):
        l = len(columns[c])
        if l == len(set(columns[c])):
            already.append([c])
            answer += 1

    now = [i for i in range(len(columns))]
    for i in range(2,len(relation[0])+1):
        comb_list = list(combinations(now,i))
        
        for cl in comb_list:
            already_check = 0
            for al in already:
                aacheck = True
                for aa in al:
                    if aa not in cl:
                        aacheck = False
                        break
                if aacheck == True:
                    already_check += 1
                    break
                        
            if already_check != 0:
                continue
            now_list = []
            check = True
            for j in range(len(relation)):
                temp = []
                for cc in cl:
                    temp.append(columns[cc][j])
                if temp not in now_list:
                    now_list.append(temp)
                else:
                    check = False
                    break

            if check == True:
                already.append(list(cl))
                answer +=1
                
    print(already)
    return answer
