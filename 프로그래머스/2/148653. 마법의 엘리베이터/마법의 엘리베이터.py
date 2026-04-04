def solution(storey):
    answer = 0
    
    while storey > 0:
        # 현재 가장 끝자리 숫자 구하기
        digit = storey % 10
        # 다음 자리 숫자 구하기 (미리 엿보기)
        next_digit = (storey // 10) % 10
        
        # 1. 5보다 큰 경우 (위로 간다)
        if digit > 5:
            answer += (10 - digit)
            storey += (10 - digit)  # 🌟 남은 층수만큼 정확히 더해서 올림 처리
            
        # 2. 딱 5인 경우 (다음 자리를 보고 판단)
        elif digit == 5:
            answer += 5
            if next_digit >= 5:
                storey += 5         # 🌟 5를 더해서 정확히 다음 10의 배수로 맞춰줌
                
        # 3. 5보다 작은 경우 (아래로 간다)
        else:
            answer += digit
            
        # 1의 자리를 깔끔하게 0으로 맞췄으니(또는 버렸으니), 10으로 나눠서 다음 자릿수로 이동
        storey //= 10
        
    return answer