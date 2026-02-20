import re

def solution(files):
    
    # 정렬 기준으로 사용할 커스텀 함수
    def parse_key(file):
        # 1. 정규표현식(re)을 사용해 '숫자'를 기준으로 문자열을 쪼갭니다.
        # [0-9]{1,5} : 0~9 범위의 숫자가 1글자 이상 5글자 이하로 연속됨을 의미 (문제 조건)
        # 괄호 '()'로 묶어주면, 기준으로 사용된 숫자 자체도 사라지지 않고 결과 리스트에 포함됩니다.
        # 예: "img0101.png" -> ["img", "0101", ".png"]
        # 예: "F-15" -> ["F-", "15", ""]
        parts = re.split(r'([0-9]{1,5})', file)
        
        # 2. 정렬 조건 1: HEAD는 대소문자를 구분하지 않음
        head = parts[0].lower()
        
        # 3. 정렬 조건 2: NUMBER는 숫자 값으로 비교 (앞의 0 무시)
        number = int(parts[1])
        
        # 4. TAIL은 정렬 기준에 영향을 주지 않으므로 반환하지 않습니다.
        # 파이썬은 튜플(head, number)을 반환하면, 첫 번째 요소로 먼저 정렬하고, 
        # 같으면 두 번째 요소로 정렬합니다.
        return (head, number)
        
    # 5. 파이썬의 내장 정렬(sorted)은 '안정 정렬(Stable Sort)'을 보장합니다.
    # 즉, head와 number가 모두 같을 경우 원래 배열에 있던 순서를 그대로 유지합니다. (문제 조건 3 완벽 충족)
    return sorted(files, key=parse_key)