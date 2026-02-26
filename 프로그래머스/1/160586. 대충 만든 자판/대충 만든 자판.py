def solution(keymap, targets):
    answer = []
    
    # 1. 각 알파벳을 치기 위한 '최소 누름 횟수'를 저장할 딕셔너리
    min_press = {}
    
    # 2. keymap을 순회하며 딕셔너리 완성하기 (사전 작업)
    for keys in keymap:
        for i, char in enumerate(keys):
            press_count = i + 1 # 인덱스는 0부터 시작하므로 누름 횟수는 +1
            
            # 딕셔너리에 해당 문자가 아직 없거나, 
            # 기존에 저장된 누름 횟수보다 지금 발견한 위치가 더 앞쪽(적은 횟수)이라면 갱신!
            if char not in min_press:
                min_press[char] = press_count
            else:
                min_press[char] = min(min_press[char], press_count)
                
    # 3. 목표 문자열(targets)들을 하나씩 확인하며 타이핑 횟수 계산
    for target in targets:
        total_press = 0
        is_possible = True
        
        for char in target:
            # 자판을 눌러서 칠 수 있는 문자인 경우
            if char in min_press:
                total_press += min_press[char]
            # 자판에 아예 없는 문자가 하나라도 껴있는 경우
            else:
                is_possible = False
                break # 더 이상 볼 필요 없이 즉시 중단
                
        # 4. 문자열 작성이 가능한 경우 총합을, 불가능했던 경우 -1을 정답 배열에 추가
        if is_possible:
            answer.append(total_press)
        else:
            answer.append(-1)
            
    return answer