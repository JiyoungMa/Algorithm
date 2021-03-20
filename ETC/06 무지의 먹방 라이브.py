import numpy

def solution(food_times, k):
    index_list = [x for x in range(len(food_times))]
    times = 0
    answer = 0

    while(times<k):
        if len(food_times)==0:
            return -1
        elif min(food_times)>(k-times)//len(food_times):
            answer = index_list[(k-times)%len(index_list)]+1
            print(answer)
            return int(answer)
        else:
            times += min(food_times)*len(food_times)
            food_times = [x-min(food_times) for x in food_times]
            zero_list = numpy.where(numpy.array(food_times) ==0)[0]
            food_times=list(numpy.delete(food_times,zero_list))
            index_list=list(numpy.delete(index_list,zero_list))
            if len(food_times)==0:
                return -1
            answer = index_list[0]+1

    print(answer)
    return int(answer)


food_times = [3,1,3]
k = 5
solution([1,1,1,1],4)