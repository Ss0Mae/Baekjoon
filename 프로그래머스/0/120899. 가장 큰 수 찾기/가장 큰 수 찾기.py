def solution(array):
    answer = []
    Max = 0
    for i in range(len(array)):
        if Max < array[i]:
            Max = array[i]
            idx = i
    answer.append(Max)
    answer.append(idx)
    return answer