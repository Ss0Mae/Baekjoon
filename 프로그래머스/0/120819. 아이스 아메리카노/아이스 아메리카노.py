def solution(money):
    answer = []
    tot = money // 5500
    mod = money % 5500
    answer.append(tot)
    answer.append(mod)
    return answer