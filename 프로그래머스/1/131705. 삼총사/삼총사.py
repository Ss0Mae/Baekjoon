from itertools import combinations

def solution(number):
    answer = 0
    # number 배열에서 3개를 뽑는 모든 조합(c)에 대하여
    for c in combinations(number, 3):
        # 그 3개의 합이 0이면 카운트 증가
        if sum(c) == 0:
            answer += 1
    return answer