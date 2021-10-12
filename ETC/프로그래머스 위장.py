def solution(clothes):
    answer = 1
    cloth_dict = dict()
    
    for cloth,types in clothes:
        if types in cloth_dict:
            cloth_dict[types] += 1
        else:
            cloth_dict[types] = 2
            
    for t in cloth_dict:
        answer *= cloth_dict[t]
    answer -= 1
    return answer
