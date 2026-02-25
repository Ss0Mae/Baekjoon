import math
def is_prime(n):
    if n < 2:
        return False
        
    # 에라토스테네스의 체 원리 응용: n의 제곱근까지만 검사하면 매우 빠릅니다.
    # int(math.sqrt(n)) + 1 까지의 숫자들로 나누어 떨어지는지 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # 한 번이라도 나누어 떨어지면 소수가 아님
            
    return True # 무사히 통과하면 소수

def solution(n):
    result = 0
    for i in range(1,n+1):
        if is_prime(i): result+=1
    
    return result