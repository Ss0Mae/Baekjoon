from collections import deque

def solution(n, vertex):
    # 1. 그래프 만들기 (인접 리스트 구조)
    # 노드 번호가 1번부터 n번까지이므로, 인덱스 계산을 편하게 하기 위해 n+1 크기로 만듭니다.
    graph = [[] for _ in range(n + 1)]
    
    # 양방향 그래프이므로 양쪽 모두에 연결 정보를 추가합니다.
    for u, v in vertex:
        graph[u].append(v)
        graph[v].append(u)
        
    # 2. 각 노드까지의 최단 거리를 저장할 배열
    # -1은 '아직 방문하지 않음'을 의미합니다.
    distances = [-1] * (n + 1)
    
    # 시작점(1번 노드)의 거리는 0으로 초기화
    distances[1] = 0
    
    # 3. BFS 탐색을 위한 큐 초기화 (시작점 1을 넣고 시작)
    queue = deque([1])
    
    # 4. BFS 본격 탐색 시작
    while queue:
        current = queue.popleft() # 현재 위치한 노드
        
        # 현재 노드와 연결된 이웃 노드들을 하나씩 확인
        for next_node in graph[current]:
            # 이웃 노드를 한 번도 방문한 적이 없다면
            if distances[next_node] == -1:
                # 거리는 (현재 노드까지의 거리 + 1)이 됩니다.
                distances[next_node] = distances[current] + 1
                # 다음 탐색을 위해 큐에 추가
                queue.append(next_node)
                
    # 5. 결과 도출
    # distances 배열에서 가장 큰 값(가장 먼 거리)을 찾습니다.
    max_distance = max(distances)
    
    # 가장 먼 거리와 동일한 값을 가진 노드가 몇 개인지 세어서 반환합니다.
    return distances.count(max_distance)