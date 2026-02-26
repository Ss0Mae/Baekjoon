from itertools import combinations
def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    
    # 2. 곱이 최대가 되려면 숫자들의 편차가 가장 작아야 합니다 (가장 균등해야 함).
    # 따라서 s를 n으로 나눈 '몫'을 기본값으로 깔고 들어갑니다.
    base = s // n
    
    # 남은 '나머지'를 1씩 쪼개서 분배해 주면 됩니다.
    rem = s % n
    
    # 3. 정답 배열 만들기
    # 문제에서 오름차순으로 정렬하라고 했으므로,
    # 작은 수인 base를 앞에 채우고, 1이 더해진 (base + 1)을 뒤에 채웁니다.
    
    # base는 총 (n - rem)개 필요하고, (base + 1)은 나머지(rem) 개수만큼 필요합니다.
    answer = [base] * (n - rem) + [base + 1] * rem
    
    return answer