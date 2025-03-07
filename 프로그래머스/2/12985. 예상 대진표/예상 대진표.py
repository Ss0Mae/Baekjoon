def solution(n, a, b):
    round_number = 0
    # a와 b가 같아질 때까지 반복 (같아지면 같은 경기로 만난 것)
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        round_number += 1
    return round_number
