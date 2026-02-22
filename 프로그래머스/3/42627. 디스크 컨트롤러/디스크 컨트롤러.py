import heapq

def solution(jobs):
    answer = 0
    current_time = 0    # 현재 시간
    completed_jobs = 0  # 완료된 작업의 수
    total_jobs = len(jobs)
    
    # 1. 요청 시간 기준으로 오름차순 정렬 (순서대로 훑기 위함)
    jobs.sort(key=lambda x: x[0])
    
    heap = []
    job_idx = 0 # 처리할 작업의 인덱스
    
    # 2. 모든 작업이 완료될 때까지 시뮬레이션 반복
    while completed_jobs < total_jobs:
        
        # 3. 현재 시간(current_time) 이전에 요청이 들어온 모든 작업을 힙에 넣음
        while job_idx < total_jobs and jobs[job_idx][0] <= current_time:
            request_time, duration = jobs[job_idx]
            # 힙 정렬의 기준을 '소요 시간(duration)'으로 하기 위해 순서를 바꿔서 넣음
            heapq.heappush(heap, (duration, request_time))
            job_idx += 1
            
        # 4. 대기 중인 작업이 있는 경우 (가장 짧은 작업 처리)
        if heap:
            duration, request_time = heapq.heappop(heap)
            current_time += duration               # 작업 소요 시간만큼 현재 시간 흐름
            answer += (current_time - request_time) # 반환 시간 = 종료 시간 - 요청 시간
            completed_jobs += 1
            
        # 5. 대기 중인 작업이 없는 경우 (다음 작업이 들어올 때까지 시간 점프)
        else:
            current_time = jobs[job_idx][0]
            
    # 6. 평균 반환 시간 계산 (소수점 이하 버림)
    return answer // total_jobs