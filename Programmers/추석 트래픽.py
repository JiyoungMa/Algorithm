def solution(lines):
    import datetime
    time_dict = dict()
    if len(lines) == 1:
        return 1
    
    for i in lines:
        now = i[:i.rfind(" ")]
        end = i[:i.rfind(" ")]
        end_datetime = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S.%f')
        sec = float(i[i.rfind(" ")+1 : -1]) - 0.001
        start_datetime = end_datetime - datetime.timedelta(seconds = sec)
        end_before = end_datetime +  datetime.timedelta(seconds = 1)
                
        for t in time_dict.keys():
            if t>start_datetime:
                time_dict[t] += 1
        if end_before not in time_dict.keys():
            time_dict[end_before] = 1

    return max(time_dict.values())
