def solution(record):
    answer = []
    id_name = dict()
    record_arr = [list(s.split(' ')) for s in record]
    for i in record_arr:
        if len(i) == 3:
            id_name[i[1]] = i[2]

    
    for i in record_arr:
        if i[0] == 'Enter':
            answer.append(id_name[i[1]] +"님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(id_name[i[1]] + "님이 나갔습니다.")
    
    return answer
