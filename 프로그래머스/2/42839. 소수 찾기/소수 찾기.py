import math
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # 한 번이라도 나누어 떨어지면 소수가 아님
            
    return True

def solution(numbers):
    # 중복된 숫자를 알아서 제거해주는 set 초기화
    # (예: "011"로 만들 수 있는 11과 "11"로 만들 수 있는 11을 하나로 합쳐줌)
    unique_nums = set()
    
    # 2. 1자리 숫자부터 최대 길이의 숫자까지 모든 경우의 수(순열) 탐색
    # 예: 길이가 3이라면 1자리, 2자리, 3자리 숫자를 모두 만들어야 합니다.
    for length in range(1, len(numbers) + 1):
        
        # 주어진 숫자 조각들로 length 길이만큼의 순열 생성
        for p in permutations(numbers, length):
            # p는 ('1', '7') 같은 튜플 형태이므로 "".join()으로 합쳐서 문자열 "17"로 만듦
            # 그리고 int()로 감싸서 정수로 변환 (이 과정에서 "011" 앞의 0이 자연스럽게 날아감)
            num = int("".join(p))
            unique_nums.add(num)
            
    # 3. set에 모인 고유한 숫자들을 하나씩 꺼내며 소수인지 판별
    answer = 0
    for n in unique_nums:
        if is_prime(n):
            answer += 1
            
    return answer