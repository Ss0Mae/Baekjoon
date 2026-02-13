from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    city_lower=[]
    
    for city in cities:
        city_lower.append(city.lower())
    #print(city_lower)
    for city in city_lower:
        if cacheSize == 0: #캐시 크기가 0이면 모든 실행에서 5초가 걸리므로 실행시간은 5 * 도시 리스트의 길이
            answer += 5 * len(city_lower)
            break
        elif city in cache: #큐 안에 참조값이 있으면(cache hit) 제거하고 다시 추가해 갱신(실행시간 1초)
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) == cacheSize: #큐가 가득 찼다면 가장 오래된 참조값을 제거하고 추가
                cache.popleft()
                cache.append(city)
                answer += 5 #참조값이 큐에 없으므로(cache miss) 실행시간 5초
            else:
                cache.append(city) #큐가 모두 채워지기 전이며 참조값이 큐에 없으므로 추가(실행시간 5초)
                answer += 5
            
    
    return answer