def solution(routes):
    # 1. 차량의 "진출 지점(나가는 위치)"을 기준으로 오름차순 정렬합니다.
    # 먼저 고속도로를 빠져나가는 차량부터 처리를 해줘야 하기 때문입니다.
    routes.sort(key=lambda x: x[1])
    #print(routes)
    answer = 0
    # 2. 마지막으로 카메라를 설치한 위치
    # 제한사항에서 차량의 진입 지점은 -30,000부터이므로 그보다 더 작은 값으로 초기화합니다.
    camera = -30001 
    
    # 3. 정렬된 차량들의 경로를 하나씩 확인합니다.
    for route in routes:
        start, end = route
        
        # 4. 현재 차량의 진입 지점이 마지막 카메라 위치보다 뒤에 있다면?
        # (기존에 설치된 카메라로는 이 차량을 찍을 수 없다는 뜻입니다)
        if start > camera:
            answer += 1    # 새로운 카메라를 한 대 꺼냅니다.
            camera = end   # ★ 핵심: 새로운 카메라는 현재 차량이 "빠져나가는 지점(end)"에 설치합니다.
            
    return answer