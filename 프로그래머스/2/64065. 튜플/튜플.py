def solution(s):
    
    sets = [set(item.split(",")) for item in s[2:-2].split("},{")]
    # 집합의 크기를 기준으로 정렬
    sets.sort(key=len)
    
    answer = []
    # 정렬된 집합 순회하며, 새로 등장한 원소만 추가
    for subset in sets:
        answer.extend(subset - set(answer))
    
    return list(map(int, answer))
