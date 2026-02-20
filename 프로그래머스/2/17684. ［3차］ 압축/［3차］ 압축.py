def solution(msg):
    answer = []
    
    # 1. 초기 사전 세팅 (A~Z를 1~26으로 매핑)
    # chr(65)는 'A', chr(90)은 'Z'입니다.
    dictionary = {chr(i + 64): i for i in range(1, 27)}
    next_idx = 27 # 다음에 사전에 추가될 단어의 색인 번호
    
    print(dictionary)
    i = 0 # 탐색을 시작할 문자열의 현재 위치
    
    # 2. 문자열 msg를 끝까지 탐색
    while i < len(msg):
        w = msg[i] # 가장 긴 단어를 저장할 변수
        j = i + 1  # 다음 글자를 확인하기 위한 끝점 인덱스
        
        # 3. 사전에 있는 가장 긴 문자열(w) 찾기
        # j를 1씩 늘려가며 자른 문자열(msg[i:j])이 사전에 있는지 확인
        while j <= len(msg) and msg[i:j] in dictionary:
            w = msg[i:j]
            j += 1
            
        # 4. 사전에 있는 단어(w)의 색인 번호를 출력(answer에 추가)
        answer.append(dictionary[w])
        
        # 5. 사전에 없는 새로운 단어(w+c)가 등장했다면 사전에 추가
        # (j가 len(msg)를 넘지 않았다면 아직 처리할 다음 글자가 남아있다는 뜻)
        if j <= len(msg):
            dictionary[msg[i:j]] = next_idx
            next_idx += 1
            
        # 6. 처리한 문자열(w)의 길이만큼 현재 위치(i)를 점프
        i += len(w)
        
    return answer