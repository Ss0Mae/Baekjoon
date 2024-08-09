def solution(arr):
    answer = 0
    n = 1                           
    
    while True:
        answer = max(arr) * n       # 가장 큰 수의 배수 기준으로 최소공배수를 구함.
        result = True               # if result=True: 최소공배수    else: 최소공배수가 아님
        for num in arr:
            if answer % num != 0:   
                result = False      # answer가 나누어 떨어지지 않으면 result=False로 변경 후 break
                break
        if result:                  # result 판별 True이면 while True문을 빠져나옴
            break                   
        n += 1
        
    return answer