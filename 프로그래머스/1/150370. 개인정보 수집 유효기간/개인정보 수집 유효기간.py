def solution(today, terms, privacies):
    answer = []
    
    # 1. 만능 날짜 변환 함수: "YYYY.MM.DD" 형태의 문자열을 총 '일(days)' 단위의 정수로 변환
    def date_to_days(date_str):
        year, month, day = map(int, date_str.split('.'))
        # 1년 = 12달 * 28일, 1달 = 28일
        return year * 12 * 28 + month * 28 + day
    
    # 2. 오늘 날짜를 일수로 변환
    today_days = date_to_days(today)
    
    # 3. 약관 종류(terms)를 딕셔너리로 저장 { "약관 종류": 유효기간(일수) }
    term_dict = {}
    for term in terms:
        t_type, t_month = term.split()
        # 약관의 달(month) 수에 28일을 곱해서 '일(days)' 단위로 저장
        term_dict[t_type] = int(t_month) * 28
        
    # 4. 각 개인정보(privacies) 만료 여부 검사
    for i, privacy in enumerate(privacies):
        date_str, p_type = privacy.split()
        
        # 수집 일자를 일수로 변환
        collected_days = date_to_days(date_str)
        
        # 파기되어야 하는 날짜 = 수집 일자 + 유효기간
        # (예: 1월 1일에 6달 유효기간이면, 7월 1일부터는 파기해야 함)
        expire_days = collected_days + term_dict[p_type]
        
        # 파기해야 하는 날짜가 오늘 날짜와 같거나 작다면 (즉, 오늘 이미 만료되었다면)
        if expire_days <= today_days:
            # 문제에서 번호는 1번부터 시작하므로 인덱스 i에 +1을 해줍니다.
            answer.append(i + 1)
            
    return answer