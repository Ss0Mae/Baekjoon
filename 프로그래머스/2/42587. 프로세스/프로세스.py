from collections import deque

def solution(priorities, location):
    # 프로세스의 원래 인덱스와 우선순위를 함께 저장
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    order = 0  # 실행 순서 카운트
    
    while queue:
        current = queue.popleft()
        # 큐에 있는 어떤 프로세스라도 현재 프로세스보다 우선순위가 높다면
        if any(current[1] < other[1] for other in queue):
            queue.append(current)
        else:
            order += 1
            # 현재 실행된 프로세스가 우리가 추적하는 프로세스이면 실행 순서를 반환
            if current[0] == location:
                return order
