from collections import Counter

def solution(want, number, discount):
    # 원하는 제품과 필요한 수량을 딕셔너리로 구성
    required = {w: n for w, n in zip(want, number)}
    window_size = sum(number)  # 항상 10
    answer = 0
    
    # 할인되는 제품 목록이 window_size보다 작으면 조건을 만족할 수 없으므로 0 리턴
    if len(discount) < window_size:
        return 0

    # 초기 윈도우의 제품 빈도 계산
    current_window = Counter(discount[:window_size])
    if current_window == required:
        answer += 1

    # 슬라이딩 윈도우를 이용하여 각 구간 검사
    for i in range(1, len(discount) - window_size + 1):
        # 윈도우에서 나가는 제품
        outgoing = discount[i - 1]
        current_window[outgoing] -= 1
        if current_window[outgoing] == 0:
            del current_window[outgoing]
        
        # 윈도우에 새로 들어오는 제품
        incoming = discount[i + window_size - 1]
        current_window[incoming] += 1
        
        # 현재 윈도우의 제품 빈도와 요구 조건 비교
        if current_window == required:
            answer += 1

    return answer
