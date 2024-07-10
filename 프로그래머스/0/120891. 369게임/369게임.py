def solution(order):
    answer = 0
    ans = ['3','6','9']
    order = str(order)
    order = list(order)
    for i in order:
        if i in ans:
            answer += 1
    return answer