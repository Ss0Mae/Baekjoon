def solution(n, k):
    answer = 0
    drink = n // 10
    k = k - drink
    answer = n * 12000 + k *2000
    return answer