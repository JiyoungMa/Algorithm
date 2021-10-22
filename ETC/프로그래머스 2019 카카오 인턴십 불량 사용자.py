from itertools import product
def solution(user_id, banned_id):
    answer = 1
    length_dict = dict()
    count_banned = [[] for _ in range(len(banned_id))]
    
    for user in user_id:
        if len(user) in length_dict:
            length_dict[len(user)].append(user)
        else:
            length_dict[len(user)] = [user]
            
    for b in range(len(banned_id)):
        banned = banned_id[b]
        search_ids = length_dict[len(banned)]
        for search in search_ids:
            check = True
            for i in range(len(banned)):
                if banned[i] != "*" and banned[i] != search[i]:
                    check = False
                    break
            if check == True:
                count_banned[b].append(search)
                
    answer_list = list(product(*count_banned))
    
    final_set = []
    
    for a in answer_list:
        if len(a) == len(set(a)):
            if set(a) not in final_set:
                final_set.append(set(a))
            
    answer = len(final_set)

    return answer
