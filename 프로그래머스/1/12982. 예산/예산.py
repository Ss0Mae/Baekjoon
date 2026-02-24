def solution(d, budget):
    answer = 0 # 가능한 부서의 수
    d.sort()
    for i in (d):
        budget -= i
        if budget < 0: 
            break
        answer += 1
    return answer