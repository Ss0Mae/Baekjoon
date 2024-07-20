def solution(left, right):
    answer = 0
    tot = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i % j ==0:
                tot+=1
        if tot %2 ==0:
            answer += i
        else: answer -= i
        tot = 0
    return answer