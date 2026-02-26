def solution(ingredient):
    answer = 0
    stack = []
    
    # 1. 재료를 순서대로 하나씩 스택(도마)에 쌓습니다.
    for i in ingredient:
        stack.append(i)
        
        # 2. 스택에 재료가 4개 이상 쌓였을 때부터 햄버거 포장 검사를 시작합니다.
        # 스택의 맨 끝(최근에 쌓인) 4개의 재료가 [빵, 야채, 고기, 빵] (1, 2, 3, 1) 인지 확인합니다.
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1 # 햄버거 1개 포장 완료
            
            # 3. 햄버거로 만들어진 4개의 재료를 스택에서 제거합니다 (폭발!).
            # del을 사용해 슬라이싱 범위 전체를 O(1)에 가깝게 한 번에 날려버릴 수 있습니다.
            # (혹은 stack.pop()을 4번 반복해도 똑같이 작동합니다.)
            del stack[-4:]
            
    return answer