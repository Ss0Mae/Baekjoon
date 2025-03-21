def solution(phone_book):
    # 전화번호를 사전순으로 정렬하면, 접두어 관계에 있는 번호들이 인접
    phone_book.sort()
    
    # 인접한 두 번호만 비교하여, 앞 번호가 뒤 번호의 접두어인지 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
