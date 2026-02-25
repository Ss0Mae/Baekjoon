from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 1. 다리를 나타내는 큐 (길이만큼 0으로 채워서 빈 공간을 표현)
    bridge = deque([0] * bridge_length)
    
    # 2. 대기 중인 트럭도 큐(deque)로 변환 (popleft()를 써서 O(1)로 빼기 위함)
    trucks = deque(truck_weights)
    
    # 3. [핵심 최적화] 현재 다리 위에 있는 트럭들의 총 무게를 기록하는 변수
    # (매번 sum(bridge)를 하면 시간 초과가 나므로 변수로 추적합니다)
    current_weight = 0
    
    # 다리 위에 트럭(또는 0)이 남아있는 동안 계속 1초씩 시뮬레이션
    while bridge:
        answer += 1 # 1초가 지남
        
        # 4. 다리 맨 앞의 칸이 다리를 빠져나감 (트럭일 수도 있고, 0일 수도 있음)
        leaving = bridge.popleft()
        current_weight -= leaving # 빠져나간 무게만큼 빼줌
        
        # 5. 아직 대기 중인 트럭이 남아있다면
        if trucks:
            # 6. 다음 트럭이 다리에 올라가도 한계 무게(weight)를 넘지 않는지 확인
            if current_weight + trucks[0] <= weight:
                # 트럭이 다리에 올라감
                next_truck = trucks.popleft()
                bridge.append(next_truck)
                current_weight += next_truck # 다리 위 무게 증가
                
            else:
                # 다음 트럭이 무거워서 못 올라가면, 
                # 다리 위 기존 트럭들을 1칸씩 앞으로 전진시키기 위해 빈 공간(0)을 추가
                bridge.append(0)
                
    # 큐가 완전히 비게 되면 시뮬레이션 종료
    return answer