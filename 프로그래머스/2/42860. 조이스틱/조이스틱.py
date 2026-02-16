def solution(name):
    # 1. 상하 이동 횟수 구하기 (Greedy)
    # 각 알파벳 별로 위로 가는 게 빠른지, 아래로(거꾸로) 가는 게 빠른지 계산해서 합산
    # 'A'는 0, 'Z'는 1이 되도록 계산 (min(순방향, 역방향))
    spell_move = 0
    for char in name:
        spell_move += min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))
        
    # 2. 좌우 이동 횟수 구하기 (완전 탐색에 가까움)
    n = len(name)
    min_move = n - 1  # 기본값: 그냥 오른쪽으로 쭉 가는 경우 (길이 - 1)
    
    for i in range(n):
        # i: 현재 위치 (여기까지 찍고 되돌아갈지 결정하는 지점)
        
        # next_i: 현재 지점(i) 다음부터 연속된 'A'를 건너뛰고 처음 만나는 'A'가 아닌 문자의 인덱스
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        # 거리 계산 3가지 케이스 비교
        # Case 1. 그냥 오른쪽으로 쭉 가기 (위에서 min_move 초기값으로 설정함)
        
        # Case 2. 오른쪽으로 갔다가(i), 다시 왼쪽으로 꺾어서 뒤쪽(n - next_i)을 공략하는 거리
        # 식: i(가는 길) + i(돌아오는 길) + (n - next_i)(뒤쪽 남은 거리)
        distance_to_back = 2 * i + (n - next_i)
        
        # Case 3. 왼쪽(뒤쪽)을 먼저 갔다가, 다시 오른쪽으로 꺾어서 오는 거리
        # 식: (n - next_i)(뒤쪽 가는 길) + (n - next_i)(다시 원점) + i(오른쪽 남은 거리)
        distance_to_front = i + 2 * (n - next_i)
        
        # 셋 중 가장 작은 값으로 갱신
        min_move = min(min_move, distance_to_back, distance_to_front)
        
    # 총 횟수 = 상하 이동 횟수 + 좌우 이동 횟수
    return spell_move + min_move