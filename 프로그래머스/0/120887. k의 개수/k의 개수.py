def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        num = str(num)
        num = list(num)
        for l in range(0,len(num)):
            if num[l] == str(k):
                answer+=1
    return answer