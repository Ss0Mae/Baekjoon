from collections import Counter

def solution(str1, str2):
    # 1. 두 글자씩 끊어서 유효한 다중집합(리스트) 만들기
    # 대소문자를 구분하지 않으므로 모두 소문자(또는 대문자)로 통일하고 시작합니다.
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 💡 꿀팁: 리스트 컴프리헨션을 사용하면 짧고 빠르게 배열을 만들 수 있습니다.
    # i부터 i+2까지 자른 2글자(chunk)가 모두 알파벳(isalpha)인 경우만 리스트에 담습니다.
    list1 = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    # 2. Counter를 활용하여 다중집합 빈도수 딕셔너리 만들기
    # 예: ['fr', 'ra', 'an', 'nc', 'ce', 'en'] -> Counter({'fr': 1, 'ra': 1, ...})
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    # 3. [핵심] 다중집합의 교집합과 합집합 구하기
    # 파이썬 Counter의 엄청난 기능: 교집합(&)과 합집합(|) 연산을 지원합니다!
    # 교집합(&): 두 Counter에 공통으로 있는 원소의 카운트 중 '최솟값(min)'을 알아서 선택
    # 합집합(|): 두 Counter에 있는 원소의 카운트 중 '최댓값(max)'을 알아서 선택
    inter = counter1 & counter2
    union = counter1 | counter2
    
    # 다중집합의 원소 개수(size)는 values()의 합으로 구합니다.
    inter_size = sum(inter.values())
    union_size = sum(union.values())
    
    # 4. 자카드 유사도 계산 및 예외 처리
    # 합집합이 0인 경우 (두 집합 모두 공집합인 경우) J(A, B) = 1로 정의됩니다.
    if union_size == 0:
        return 65536
        
    # 공식에 따라 (교집합 / 합집합) * 65536 후 소수점 아래를 버리고 정수(int)로 반환
    answer = int((inter_size / union_size) * 65536)
    return answer