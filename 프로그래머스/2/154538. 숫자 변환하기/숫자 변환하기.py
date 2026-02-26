from collections import deque

def solution(x, y, n):
    # 시작 숫자와 목표 숫자가 이미 같다면 0번 연산
    if x == y:
        return 0
        
    # 큐에는 (현재 숫자, 지금까지의 연산 횟수)를 튜플로 저장
    q = deque([(x, 0)])
    
    print(q)
    # 중복 계산 방지(시간 초과 방지)를 위한 방문 기록 set
    visited = set([x])
    
    while q:
        curr_val, steps = q.popleft()
        
        # 3가지 연산(가지치기)을 순회
        for next_val in (curr_val + n, curr_val * 2, curr_val * 3):
            # 목표 숫자에 도달했다면 즉시 현재까지의 횟수 + 1 반환
            if next_val == y:
                return steps + 1
                
            # 목표 숫자보다 작고, 한 번도 만들어본 적 없는 숫자일 때만 큐에 추가
            # (next_val > y 인 경우는 어차피 y를 지나친 것이므로 버림)
            if next_val < y and next_val not in visited:
                visited.add(next_val)
                q.append((next_val, steps + 1))
                
    # 큐가 다 빌 때까지 y를 만들지 못했다면
    return -1