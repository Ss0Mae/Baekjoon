def solution(elements):
    n = len(elements)
    doubled = elements * 2  # 원형 수열 처리를 위한 더블 배열
    distinct_sums = set()
    
    for i in range(n):
        current_sum = 0
        # 최대 n개 원소를 더하는 경우까지만 확인
        for j in range(i, i + n):
            current_sum += doubled[j]
            distinct_sums.add(current_sum)

    return len(distinct_sums)
