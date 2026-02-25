def solution(k, m, score):
    # 1. 가장 비싼 사과부터 포장하기 위해 내림차순 정렬합니다.
    # O(N log N)이 걸리며 N이 1,000,000이므로 충분히 통과합니다.
    score.sort(reverse=True)
    
    answer = 0
    
    # 2. 파이썬의 range(start, stop, step)을 활용한 점프!
    # m개씩 묶었을 때, 각 상자에서 가장 낮은 점수는 항상 묶음의 맨 마지막 사과입니다.
    # 인덱스는 0부터 시작하므로 첫 상자의 마지막 사과 인덱스는 (m - 1)입니다.
    # 거기서부터 m칸씩 건너뛰면 다음 상자의 마지막 사과를 바로바로 찾을 수 있습니다.
    for i in range(m - 1, len(score), m):
        
        # 상자의 가격 = (가장 낮은 점수) * (사과 개수 m)
        answer += score[i] * m
        
    return answer