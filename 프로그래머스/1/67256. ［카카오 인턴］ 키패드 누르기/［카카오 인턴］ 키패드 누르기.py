def solution(numbers, hand):
    answer = ''
    
    # 1. 키패드를 2차원 좌표(x, y)로 매핑한 딕셔너리
    # 위에서부터 아래로 행(0,1,2,3), 왼쪽에서 오른쪽으로 열(0,1,2)
    key_dict = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 2. 왼손과 오른손의 초기 위치 설정
    left_pos = key_dict['*']
    right_pos = key_dict['#']
    
    # 3. 눌러야 할 번호들을 순회하며 손가락 이동
    for n in numbers:
        # [조건 1] 왼쪽 열 (1, 4, 7)은 무조건 왼손
        if n in [1, 4, 7]:
            answer += 'L'
            left_pos = key_dict[n]  # 왼손 위치 갱신
            
        # [조건 2] 오른쪽 열 (3, 6, 9)는 무조건 오른손
        elif n in [3, 6, 9]:
            answer += 'R'
            right_pos = key_dict[n] # 오른손 위치 갱신
            
        # [조건 3] 가운데 열 (2, 5, 8, 0)은 더 가까운 손
        else:
            target_pos = key_dict[n]
            
            # 거리 계산 (맨해튼 거리: |x1 - x2| + |y1 - y2|)
            left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
            
            # 거리가 더 가까운 쪽을 선택
            if left_dist < right_dist:
                answer += 'L'
                left_pos = target_pos
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = target_pos
                
            # 거리가 같다면, 사용자의 주 손(hand)을 선택
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = target_pos
                else:
                    answer += 'R'
                    right_pos = target_pos
                    
    return answer