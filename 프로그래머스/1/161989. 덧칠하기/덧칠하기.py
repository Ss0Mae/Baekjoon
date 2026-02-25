def solution(n, m, section):
    answer = 0
    painted_until = 0 # 롤러가 칠해진 마지막 위치(어디까지 칠했는지)를 저장
    
    # 칠해야 할 구역을 앞에서부터 하나씩 확인
    for s in section:
        # 현재 확인 중인 구역(s)이 이전에 칠해둔 영역(painted_until)보다 크다면
        # 즉, 아직 페인트칠이 되지 않은 곳을 발견했다면!
        if s > painted_until:
            answer += 1 # 롤러질 횟수 1 증가
            
            # 여기서부터 롤러(길이 m)로 칠하면, 
            # 현재 위치(s)부터 (s + m - 1) 위치까지 한 번에 칠해집니다.
            # 예: s가 2이고 m이 4라면 -> 2, 3, 4, 5까지 칠해짐 (2 + 4 - 1 = 5)
            painted_until = s + m - 1
            
    return answer