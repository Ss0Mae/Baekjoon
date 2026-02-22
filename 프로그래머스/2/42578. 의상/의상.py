from collections import Counter

def solution(clothes):
    # 1. 의상의 종류별로 빈도수(개수)를 셉니다.
    # clothes는 [[이름, 종류], [이름, 종류]...] 형태입니다.
    # 리스트 컴프리헨션을 사용해 '종류(type)'만 쏙 뽑아낸 뒤 Counter에 넣습니다.
    # 결과 예시: Counter({'headgear': 2, 'eyewear': 1})
    counter = Counter([type for name, type in clothes])
    
    # 2. 모든 조합의 수를 계산할 변수 (곱셈을 해야 하므로 1로 시작)
    answer = 1
    
    # 3. 수식 적용: (해당 종류의 옷 개수 + 안 입는 경우 1)을 모두 곱해줍니다.
    for count in counter.values():
        answer *= (count + 1)
        
    # 4. '최소 한 개의 의상은 입습니다' 조건 처리
    # 모든 종류의 옷을 하나도 입지 않은 최악의 경우(1가지)를 빼줍니다.
    return answer - 1