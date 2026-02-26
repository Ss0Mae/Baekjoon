def solution(n):
    answer = ''
    
    while n > 0:
        remainder = n % 3
        
        # 나머지가 1이나 2면 그대로 1, 2를 붙이고 몫을 취함
        if remainder == 1:
            answer = '1' + answer
            n //= 3
        elif remainder == 2:
            answer = '2' + answer
            n //= 3
            
        # 나머지가 0일 때가 124 나라의 핵심!
        elif remainder == 0:
            answer = '4' + answer
            # 딱 나누어 떨어지면 다음 자릿수로 넘어갈 때 '자리내림(Borrow)'이 필요하므로 몫에서 1을 뺌
            n = (n // 3) - 1
            
    return answer