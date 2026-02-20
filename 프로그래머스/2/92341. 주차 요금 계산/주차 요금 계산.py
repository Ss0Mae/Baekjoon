import math

# 1. 시간 문자열(HH:MM)을 '분(minute)' 단위의 정수로 변환하는 헬퍼 함수
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    in_time = {}      # 현재 주차 중인 차량의 입차 시간 {차량번호: 입차분}
    total_time = {}   # 차량별 하루 누적 주차 시간 {차량번호: 누적분}
    
    # 2. 입출차 기록(records) 처리
    for record in records:
        time_str, car_num, status = record.split()
        minutes = time_to_minutes(time_str)
        
        if status == "IN":
            in_time[car_num] = minutes
            # 처음 들어온 차량이면 누적 시간 딕셔너리 0으로 초기화
            if car_num not in total_time:
                total_time[car_num] = 0
                
        elif status == "OUT":
            # 주차 시간 = 출차 시간(minutes) - 입차 시간(in_time[car_num])
            parked_time = minutes - in_time[car_num]
            total_time[car_num] += parked_time
            del in_time[car_num] # 출차 처리 완료되었으므로 in_time에서 삭제
            
    # 3. 출차 기록이 없는(in_time에 남아있는) 차량 처리
    # 23:59는 분으로 환산하면 23 * 60 + 59 = 1439분
    max_time = 23 * 60 + 59 
    for car_num, minutes in in_time.items():
        parked_time = max_time - minutes
        total_time[car_num] += parked_time
        
    # 4. 요금 계산 및 차량 번호순 정렬
    answer = []
    # total_time.keys() (차량 번호들)를 정렬하여 순서대로 처리
    for car_num in sorted(total_time.keys()):
        t = total_time[car_num] # 누적 주차 시간
        
        # 기본 시간 이하라면 기본 요금만
        if t <= base_time:
            fee = base_fee
        # 기본 시간을 초과했다면 추가 요금 계산 (올림 처리)
        else:
            # math.ceil을 사용하여 소수점 올림 처리
            extra_time = t - base_time
            fee = base_fee + math.ceil(extra_time / unit_time) * unit_fee
            
        answer.append(fee)
        
    return answer