def solution(N, stages):
    # 1. 스테이지별 멈춰있는 플레이어 수를 미리 계산 (시간 복잡도 최적화)
    # N+2 칸을 만드는 이유: N+1(모두 클리어한 사람)까지 인덱스로 접근하기 위함
    counts = [0] * (N + 2)
    
    for stage in stages:
        counts[stage] += 1
            
    answer = []
    total_players = len(stages) # 처음 1번 스테이지에 도달한 전체 플레이어 수
    
    # 2. 1번부터 N번 스테이지까지 돌면서 실패율 계산
    for i in range(1, N + 1):
        count = counts[i] # 현재 스테이지에 멈춰있는 사람 수
        
        # 3. 함정 방어: 도달한 플레이어가 0명일 때의 예외 처리
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = count / total_players
            
        answer.append((i, fail_rate)) # (스테이지 번호, 실패율) 튜플 형태로 저장
        
        # 4. 다음 스테이지 도달자 수 갱신 (현재 스테이지에 멈춘 사람 빼기)
        total_players -= count
        
    # 5. 다중 조건 정렬: 실패율(x[1]) 내림차순, 실패율이 같으면 스테이지 번호(x[0]) 오름차순
    answer.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 결과에서 스테이지 번호만 순서대로 뽑아서 리스트로 반환
    return [stage[0] for stage in answer]