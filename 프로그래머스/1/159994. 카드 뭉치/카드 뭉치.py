def solution(cards1, cards2, goal):
    # 각 카드 뭉치의 맨 앞(사용할 차례)을 가리키는 인덱스 포인터
    idx1 = 0
    idx2 = 0
    
    # 만들어야 하는 목표 문장(goal)의 단어들을 하나씩 순서대로 확인
    for word in goal:
        
        # 1. cards1의 카드를 쓸 수 있는지 확인
        # (인덱스가 범위를 벗어나지 않았고, 맨 앞 카드가 찾는 단어와 일치하는 경우)
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1 # 카드를 썼으므로 다음 카드로 포인터 이동
            
        # 2. cards2의 카드를 쓸 수 있는지 확인
        # (위와 동일한 조건 검사)
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1 # 카드를 썼으므로 다음 카드로 포인터 이동
            
        # 3. 양쪽 카드 뭉치 맨 앞의 카드 중 어느 것도 쓸 수 없는 경우
        else:
            return "No" # 더 이상 문장을 만들 수 없음
            
    # goal의 모든 단어를 무사히 찾았다면
    return "Yes"