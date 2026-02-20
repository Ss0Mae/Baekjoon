def solution(survey, choices):
    # 1. 성격 유형별 점수를 저장할 딕셔너리 초기화
    # 8개의 알파벳에 대해 모두 0점으로 시작합니다.
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 2. 질문(survey)과 선택지(choices)를 동시에 묶어서 순회 (zip 활용)
    for s, choice in zip(survey, choices):
        disagree_type = s[0] # 비동의 시 점수를 얻는 유형 (첫 번째 글자)
        agree_type = s[1]    # 동의 시 점수를 얻는 유형 (두 번째 글자)
        
        # 3. 점수 계산 로직
        if choice < 4:
            # 1, 2, 3번 선택지 (비동의) -> 첫 번째 글자에 점수 누적
            # 1번: 3점, 2번: 2점, 3번: 1점이므로 (4 - choice)로 깔끔하게 계산
            scores[disagree_type] += (4 - choice)
            
        elif choice > 4:
            # 5, 6, 7번 선택지 (동의) -> 두 번째 글자에 점수 누적
            # 5번: 1점, 6번: 2점, 7번: 3점이므로 (choice - 4)로 계산
            scores[agree_type] += (choice - 4)
            
        # choice가 4인 경우는 점수 이동이 없으므로 무시합니다.
            
    # 4. 4개의 지표를 비교하여 최종 성격 유형 결정
    answer = ''
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for type1, type2 in indicators:
        # 두 점수를 비교합니다.
        # 문제 조건: "점수가 같으면 사전순으로 빠른 성격 유형을 선택한다"
        # 위 indicators 배열에 미리 '사전순으로 빠른 알파벳'을 type1 자리에 두었으므로,
        # 크거나 같은지(>=)만 판별하면 예외 처리 없이 깔끔하게 해결됩니다.
        if scores[type1] >= scores[type2]:
            answer += type1
        else:
            answer += type2
            
    return answer