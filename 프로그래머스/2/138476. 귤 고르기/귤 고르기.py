from collections import Counter

def solution(k, tangerine):
    answer = 0
    # 귤 크기별 빈도 계산 후, 빈도가 높은 순으로 정렬
    sorted_counts = sorted(Counter(tangerine).values(), reverse=True)
    
    for count in sorted_counts:
        k -= count
        answer += 1
        if k <= 0:
            break
    return answer
