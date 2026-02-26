def solution(s, skip, index):
    answer = ''
    
    # 1. 전체 알파벳 문자열 준비
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # 2. skip에 포함되지 않은 '유효한 알파벳'만 남긴 리스트 생성 (핵심 로직)
    # 예: skip이 "wbqd"라면, 저 4개의 글자가 쏙 빠진 리스트가 만들어집니다.
    valid_alphabet = [c for c in alphabet if c not in skip]
    #print(valid_alphabet)
    # 3. 문자열 s를 한 글자씩 순회하며 변환
    for char in s:
        # 현재 글자가 유효 알파벳 리스트에서 몇 번째(인덱스)에 있는지 찾기
        curr_idx = valid_alphabet.index(char)
        
        # index만큼 뒤로 이동
        # 리스트의 길이를 넘어가면 다시 처음으로 돌아오게 하기 위해 모듈러(%) 연산 사용
        new_idx = (curr_idx + index) % len(valid_alphabet)
        
        # 변환된 새 알파벳을 정답에 이어 붙이기
        answer += valid_alphabet[new_idx]
        
    return answer