# def solution(n):
#     answer = 0
#     for i in range(1,n+1):
#         sum = 0
#         for j in range(i,n+1):
#             sum += j
#             if sum == n:
#                 answer+=1
#                 break
#             elif sum > n:
#                 break
#     return answer
# ==========================================
# 풀이 1: 투 포인터 느낌의 정석 풀이 (추천)
# ==========================================
def solution(n):
    answer = 0
    
    # 1. 1부터 목표 숫자 n의 절반(n // 2)까지만 탐색합니다.
    # 절반을 넘는 두 자연수를 더하면 무조건 n보다 커지기 때문입니다.
    # (예: n이 15라면, 8 + 9 = 17이므로 8 이상은 검사할 필요가 없음)
    for i in range(1, (n // 2) + 1):
        total_sum = 0
        
        # 2. i부터 1씩 증가하며 연속된 수를 더해갑니다.
        for j in range(i, n + 1):
            total_sum += j
            
            # 3. 더한 합이 n과 정확히 같다면 카운트 증가 후 종료
            if total_sum == n:
                answer += 1
                break
                
            # 4. 더한 합이 n을 넘어가면 더 이상 볼 필요 없으므로 즉시 종료 (핵심 최적화)
            elif total_sum > n:
                break
                
    # 5. 자기 자신(n) 1개로 이루어진 경우도 1가지 방법에 포함되므로 +1 해줍니다.
    return answer + 1