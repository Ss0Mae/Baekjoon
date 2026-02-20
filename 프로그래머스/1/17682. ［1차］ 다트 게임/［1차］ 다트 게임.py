def solution(dartResult):
    stack = []
    
    # 1. 파싱 꿀팁: 두 자리 숫자인 '10'을 한 글자인 'X'로 치환해 둡니다.
    # 이렇게 하면 무조건 한 글자씩 잘라서 처리할 수 있습니다.
    dartResult = dartResult.replace('10', 'X')
    
    # 2. 보너스(S, D, T) 계산을 쉽게 하기 위한 딕셔너리
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    
    # 3. 문자열을 한 글자씩 순회하며 스택에 점수 쌓기
    for i in dartResult:
        
        # [Case 1] 숫자인 경우 (점수)
        if i.isdigit() or i == 'X':
            if i == 'X':
                stack.append(10) # X는 10점으로 스택에 넣음
            else:
                stack.append(int(i)) # 일반 숫자는 정수로 변환해서 넣음
                
        # [Case 2] 보너스(S, D, T)인 경우
        elif i in bonus_dict:
            # 스택의 맨 위 점수를 꺼내서 제곱 계산 후 다시 넣음
            num = stack.pop()
            stack.append(num ** bonus_dict[i])
            
        # [Case 3] 옵션(*)인 경우
        elif i == '*':
            # 현재 점수(맨 위) 2배
            num = stack.pop()
            
            # 이전 점수(그다음 맨 위)가 있다면 그것도 2배
            if stack:
                stack[-1] *= 2
                
            stack.append(num * 2) # 아까 뽑은 현재 점수 다시 넣기
            
        # [Case 4] 옵션(#)인 경우
        elif i == '#':
            # 스택 맨 위의 점수를 마이너스로 만듦
            stack[-1] *= -1

    # 4. 스택에 쌓인 모든 점수(최대 3개)의 합을 반환
    return sum(stack)