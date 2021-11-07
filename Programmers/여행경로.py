from collections import deque
import copy
def solution(tickets):
    answer = []
    graph_dict = dict()
    
    for departure, arrival in tickets:
        if departure in graph_dict:
            graph_dict[departure].append(arrival)
        else:
            graph_dict[departure] = [arrival]


    queue = deque([("ICN",["ICN"],graph_dict)])

    
    while queue:
        now, now_list, now_graph = queue.popleft()
        
        if now in now_graph and len(now_graph[now]) > 0:
            for g in now_graph[now]:
                new_graph = copy.deepcopy(now_graph)
                new_graph[now].remove(g)
                new_list = now_list + [g]
                queue.append((g,new_list,new_graph))
        else:
            check = True
            for g in now_graph:
                if len(now_graph[g])>0:
                    check = False
                    break
            if check == True:
                answer.append(now_list)
            
    answer.sort()
    
    return answer[0]
