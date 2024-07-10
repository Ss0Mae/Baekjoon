def solution(num, k):
    answer = -1
    num = str(num)
    num = list(num)
    for i in range(len(num)):
        if num[i] == str(k): 
            answer = i +1
            break
    return answer