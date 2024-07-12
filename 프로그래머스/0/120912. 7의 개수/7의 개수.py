def solution(array):
    answer = 0
    for i in array:
        i = str(i)
        i = list(i)
        for j in range(len(i)):
            if i[j] == '7':
                answer+=1
    return answer