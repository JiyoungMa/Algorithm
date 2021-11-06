def solution(bridge_length, weight, truck_weights):
    answer = 1
    now_weight = 0
    now_trucks = 0
    start_times = [0] * len(truck_weights)
    i = 0
    while i < len(truck_weights):
        for j in range(i-now_trucks,i,1):
            if bridge_length + start_times[j] <= answer:
                now_trucks -= 1
                now_weight -= truck_weights[j]
        if now_weight + truck_weights[i] <= weight and now_trucks+1 <=bridge_length:
            start_times[i] = answer
            now_weight += truck_weights[i]
            now_trucks += 1
            answer += 1
            i+= 1
        else:
            answer = bridge_length + start_times[i-now_trucks]
            now_weight -= truck_weights[i-now_trucks]
            now_trucks -= 1
            
    for i in range(len(truck_weights)-now_trucks,len(truck_weights),1):
        answer = bridge_length + start_times[i]
    return answer
