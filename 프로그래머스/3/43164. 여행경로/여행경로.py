from collections import defaultdict

def solution(tickets):
    # 1. 그래프 만들기 (딕셔너리)
    # Key: 출발 공항, Value: 도착 공항 리스트
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    print(graph)
    
    # 2. 도착 공항 리스트를 역순 정렬
    # (알파벳 순서가 앞서는 것을 나중에 pop해서 먼저 방문하기 위함)
    for key in graph.keys():
        graph[key].sort(reverse=True)
    

    stack = ["ICN"] # 시작은 항상 인천
    path = []       # 최종 경로를 담을 리스트
    
    # 3. DFS 탐색 (스택 빌 때까지)
    while stack:
        # 스택의 맨 위(현재 있는 공항)를 살짝 봅니다.
        top = stack[-1]
        
        # 3-1. 현재 공항에서 갈 수 있는 티켓이 남아있다면?
        if top in graph and graph[top]:
            # 알파벳 순서가 가장 빠른 도착지를 꺼내서 스택에 넣음 (이동)
            stack.append(graph[top].pop())
            
        # 3-2. 더 이상 갈 곳이 없다면? (막다른 길 or 모든 티켓 소진)
        else:
            # 경로에 추가하고 스택에서 제거 (역순으로 쌓임)
            path.append(stack.pop())
            
    # 4. 역순으로 쌓인 경로를 뒤집어서 반환
    return path[::-1]