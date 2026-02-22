def solution(n, costs):
    # 1. 다리 건설 비용을 기준으로 오름차순 정렬 (싼 다리부터 지어야 하므로)
    # costs의 원소는 [섬1, 섬2, 비용] 형태이므로 인덱스 2(비용)를 기준으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # 각 섬의 연결 상태(소속된 그룹의 부모)를 기록할 배열
    # 처음에는 모든 섬이 자기 자신을 부모로 가짐 (아무도 연결되지 않은 상태)
    parent = [i for i in range(n)]
    
    # ---------------------------------------------------------
    # [Union-Find 핵심 함수 1] Find: 특정 섬이 속한 그룹의 '최상위 부모'를 찾음
    def find_parent(parent, x):
        if parent[x] != x:
            # 경로 압축(Path Compression) 기법: 찾으면서 부모를 최상위 부모로 갱신
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
        
    # [Union-Find 핵심 함수 2] Union: 두 섬을 하나의 그룹으로 연결
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        # 더 작은 번호를 가진 섬을 부모로 설정하는 것이 일반적인 관례입니다.
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    # ---------------------------------------------------------
    
    answer = 0
    edges_used = 0 # 현재까지 지은 다리의 개수
    
    # 2. 정렬된 다리를 비용이 싼 것부터 하나씩 확인
    for island1, island2, cost in costs:
        
        # 3. 사이클(Cycle) 검사
        # 두 섬의 최상위 부모가 다르다면 -> 아직 서로 연결되지 않았다는 뜻!
        if find_parent(parent, island1) != find_parent(parent, island2):
            # 다리를 짓고 두 섬을 같은 그룹으로 묶음 (Union)
            union_parent(parent, island1, island2)
            answer += cost       # 총비용에 추가
            edges_used += 1      # 지은 다리 개수 증가
            
            # 다리를 (섬의 개수 - 1)개 지었다면 모든 섬이 연결된 것이므로 조기 종료
            if edges_used == n - 1:
                break
                
    return answer