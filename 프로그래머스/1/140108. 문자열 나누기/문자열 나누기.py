def solution(s):
    answer = 0
    x = ''          # 현재 부분 문자열의 첫 글자
    x_count = 0     # 첫 글자(x)가 나온 횟수
    other_count = 0 # 다른 글자가 나온 횟수
    
    for char in s:
        # 1. 새로운 덩어리가 시작될 때 첫 글자 설정
        if x == '':
            x = char
            
        # 2. 글자 종류에 따라 카운트 증가
        if char == x:
            x_count += 1
        else:
            other_count += 1
            
        # 3. 두 카운트 횟수가 같아지는 순간 분리
        if x_count == other_count:
            answer += 1    # 분리된 문자열 개수 1 증가
            
            # 다음 덩어리를 검사하기 위해 변수들 초기화
            x = ''
            x_count = 0
            other_count = 0
            
    # 4. 문자열 끝까지 읽었는데 두 횟수가 다르게 남은 덩어리가 있는 경우
    # (x가 빈 문자열이 아니라는 뜻은 아직 초기화되지 않은 잔여물이 있다는 의미입니다)
    if x != '':
        answer += 1
        
    return answer