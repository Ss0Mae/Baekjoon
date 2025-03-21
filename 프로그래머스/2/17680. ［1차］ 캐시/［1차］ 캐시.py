from collections import deque

def solution(cacheSize, cities):
    # 캐시 크기가 0이면 모든 요청이 miss 처리되므로 바로 결과 반환
    if cacheSize == 0:
        return 5 * len(cities)
    
    answer = 0
    cache = deque()
    
    # 도시 이름을 순회하며 처리 (모두 소문자로 변환)
    for city in (city.lower() for city in cities):
        if city in cache:
            # 캐시 히트: 기존의 위치에서 제거하고 맨 뒤에 추가하여 최근 사용 갱신
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            # 캐시 미스: 캐시가 꽉 찼으면 가장 오래된 항목 제거
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
            
    return answer
