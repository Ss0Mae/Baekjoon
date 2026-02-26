def solution(lottos, win_nums):
    # 1. 알아볼 수 없는 번호(0)의 개수 카운트
    zero_count = lottos.count(0)
    
    # 2. 확실하게 당첨 번호와 일치하는 번호의 개수 카운트
    # 파이썬의 set 교집합(&)을 이용하면 for문 없이 한 줄로 개수를 구할 수 있습니다.
    # (0은 win_nums에 애초에 없으므로 자연스럽게 무시됩니다)
    match_count = len(set(lottos) & set(win_nums))
    
    # 3. [핵심 꿀팁] 맞힌 개수에 따른 순위 배열
    # 배열의 '인덱스'가 '맞힌 개수'를 의미하고, '값'이 '순위'를 의미하도록 세팅합니다.
    # 예: 0개 맞히면 6등, 1개 맞히면 6등, 2개 맞히면 5등 ... 6개 맞히면 1등
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    # 4. 최고 순위와 최저 순위 계산
    # 최고 순위: 이미 맞힌 개수 + 지워진 번호(0)가 전부 당첨 번호일 경우
    max_rank = rank[match_count + zero_count]
    
    # 최저 순위: 지워진 번호(0)가 전부 꽝일 경우 (현재 맞힌 개수 그대로 유지)
    min_rank = rank[match_count]
    
    return [max_rank, min_rank]