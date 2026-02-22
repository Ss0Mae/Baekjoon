def solution(phone_book):
    # 1. 문자열 정렬 (사전 순으로 정렬됨)
    # 정렬을 하면 접두어가 겹치는 번호들은 무조건 인접하게 배치됩니다.
    # 예: ["119", "119552", "12", "123"]
    phone_book.sort()
    
    # 2. 이중 루프 대신, 바로 옆에 있는(인접한) 번호 1개와만 비교합니다.
    for i in range(len(phone_book) - 1):
        # 앞 번호가 바로 뒷 번호의 접두어인지 확인
        # 파이썬의 startswith() 함수를 쓰면 매우 쉽게 확인 가능합니다.
        if phone_book[i+1].startswith(phone_book[i]):
            return False # 접두어인 경우가 발견되면 즉시 False 반환
            
    return True # 무사히 다 통과했다면 True