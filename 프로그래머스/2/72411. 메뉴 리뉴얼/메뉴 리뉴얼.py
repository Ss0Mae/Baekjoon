from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 1. 코스 요리를 구성할 단품메뉴들의 개수(course_size)마다 반복
    for course_size in course:
        menu_combinations = []
        
        # 2. 각 손님의 주문(order)에서 course_size만큼의 조합을 뽑아냄
        for order in orders:
            # 주문한 메뉴를 알파벳 순으로 정렬 ('XW'와 'WX'가 같은 조합인 'W', 'X'로 묶이게 하기 위함)
            sorted_menu = sorted(order)
            
            # Canvas의 조합(combinations) 치트키 활용
            # sorted_menu에서 course_size만큼 뽑은 모든 조합을 menu_combinations 리스트에 이어붙임
            menu_combinations.extend(combinations(sorted_menu, course_size))
            
        # 3. 뽑아낸 모든 조합들의 등장 빈도수를 셈
        # 예: Counter({('A', 'C'): 4, ('C', 'D'): 3, ...})
        counter = Counter(menu_combinations)
        # 조합이 하나라도 만들어졌다면 처리 (비어있는 경우 max()에서 에러 발생 방지)
        if counter:
            # 4. 가장 많이 주문된 조합의 횟수를 찾음
            max_count = max(counter.values())
            
            # 5. 문제 조건: "최소 2명 이상의 손님으로부터 주문된 조합에 대해서만 코스요리 후보에 포함"
            if max_count >= 2:
                for menu, count in counter.items():
                    if count == max_count:
                        # 튜플 형태인 ('A', 'C')를 문자열 'AC'로 합쳐서 정답에 추가
                        answer.append(''.join(menu))
                        
    # 6. 최종적으로 코스요리 메뉴 구성을 사전 오름차순으로 정렬하여 반환
    return sorted(answer)