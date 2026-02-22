import math

def solution(progresses, speeds):
    answer = []
    
    # 1. 각 기능이 완료되기까지 남은 '일수(Days)'를 먼저 계산합니다.
    days_left = []
    for p, s in zip(progresses, speeds):
        # (100 - 현재 진도) / 속도를 한 후 올림 처리
        days = math.ceil((100 - p) / s)
        days_left.append(days)
        
    # 예시: days_left가 [7, 3, 9] 라고 가정해봅시다.
    
    # 2. 첫 번째 작업을 기준으로 배포 그룹을 묶기 시작합니다.
    current_max_day = days_left[0] # 현재 배포 그룹의 기준일 (가장 오래 걸리는 작업)
    count = 0 # 이번 배포에 포함될 기능의 수
    
    for day in days_left:
        # 뒤에 있는 작업이 기준일보다 일찍 끝나거나 동시에 끝난다면
        # 앞 작업이 배포될 때까지 기다렸다가 함께 배포되어야 함
        if day <= current_max_day:
            count += 1
            
        # 뒤에 있는 작업이 기준일보다 늦게 끝난다면
        # 이전까지 묶였던 작업들을 먼저 배포하고, 새로운 배포 그룹을 시작함
        else:
            answer.append(count)  # 이전 묶음 배포
            count = 1             # 새로운 그룹의 첫 번째 작업
            current_max_day = day # 기준일을 새로운 작업의 일수로 갱신
            
    # 3. 마지막으로 묶여있던 배포 그룹도 마저 배열에 넣어줍니다.
    answer.append(count)
    
    return answer