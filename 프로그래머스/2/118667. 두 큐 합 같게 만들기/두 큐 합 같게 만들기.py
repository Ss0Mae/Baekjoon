from collections import deque

def solution(queue1, queue2):
    # 1. 일반 리스트를 deque로 변환 (popleft의 시간 복잡도를 O(1)로 만들기 위함)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 2. 초기 합계 계산 (매번 sum()을 호출하지 않기 위해 변수에 저장)
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # 총합이 홀수라면, 절대 두 큐의 합을 같게 만들 수 없으므로 즉시 종료
    if (sum1 + sum2) % 2 != 0:
        return -1
        
    answer = 0
    # 무한 루프 방지용 한계치 (Limit) 설정
    # 두 큐의 모든 원소가 자리를 바꾸고도 남을 충분한 횟수 (보통 큐 길이의 3~4배)
    limit = len(queue1) * 4 
    
    # 3. 두 큐의 합이 같아질 때까지 반복 (Greedy 알고리즘 적용)
    while sum1 != sum2:
        # 한계치를 넘어가면 도저히 같게 만들 수 없는 경우임
        if answer > limit:
            return -1
            
        # q1의 합이 더 크면, q1에서 빼서 q2로 넘김
        if sum1 > sum2:
            val = q1.popleft()
            q2.append(val)
            sum1 -= val   # 이동한 값만큼 sum1은 감소
            sum2 += val   # 이동한 값만큼 sum2는 증가
            
        # q2의 합이 더 크면, q2에서 빼서 q1으로 넘김
        else:
            val = q2.popleft()
            q1.append(val)
            sum2 -= val
            sum1 += val
            
        answer += 1 # 작업 횟수 증가
        
    return answer