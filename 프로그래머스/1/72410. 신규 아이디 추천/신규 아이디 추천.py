def solution(new_id):
    # 1단계: 모든 대문자를 대응되는 소문자로 치환
    answer = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    # 정규표현식 대신 for문과 조건문(islower, isdigit 등)을 사용하여 허용된 문자만 이어붙입니다.
    temp = ""
    for char in answer:
        if char.islower() or char.isdigit() or char in ['-', '_', '.']:
            temp += char
    answer = temp
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    # '..' 문자열이 answer 안에 존재하는 동안 계속 '.'으로 교체합니다.
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')
    
    # 5단계: 빈 문자열이라면, "a"를 대입
    if not answer:
        answer = 'a'
        
    # 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) >= 16:
        answer = answer[:15]
        # 슬라이싱 후 끝에 남은 마침표를 rstrip으로 깔끔하게 제거
        answer = answer.rstrip('.')
        
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer