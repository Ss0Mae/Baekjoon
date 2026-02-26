from collections import Counter

def solution(X, Y):
    # 1. X와 Y의 각 숫자(0~9) 빈도수를 셉니다. (O(N)의 시간 복잡도로 매우 빠름)
    count_x = Counter(X)
    count_y = Counter(Y)
    
    answer = []
    
    # 2. 가장 큰 수를 만들어야 하므로 9부터 0까지 역순으로 내려가며 확인합니다.
    for i in range(9, -1, -1):
        digit = str(i)
        
        # 두 문자열에 공통으로 존재하는 숫자인 경우
        if digit in count_x and digit in count_y:
            
            # 짝을 지어야 하므로 공통으로 나타난 횟수 중 '최솟값'을 구함
            common_count = min(count_x[digit], count_y[digit])
            
            # 숫자 문자열을 횟수만큼 반복해서 리스트에 추가 (예: "9" * 3 = "999")
            answer.append(digit * common_count)
            
    # 3. 공통 숫자가 하나도 없어서 배열이 비어있는 경우
    if not answer:
        return "-1"
        
    # 4. 리스트에 담긴 문자열 조각들을 하나로 합쳐줍니다.
    # (매번 += 로 문자열을 더하는 것보다 join을 쓰는 것이 파이썬에서 훨씬 빠릅니다)
    result = "".join(answer)
    
    # 5. [핵심 함정] 0으로만 구성된 경우 (예: "00", "000")
    # 내림차순으로 붙였으므로, 맨 앞 글자가 '0'이라는 것은 뒤에도 전부 '0'이라는 뜻입니다.
    if result[0] == '0':
        return "0"
        
    return result