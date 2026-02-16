# from collections import deque

# def solution(begin, target, words):
    
#     if target not in words:
#         return 0
    
#     queue = deque([(begin, 0)])
#     visited = [False] * len(words)
    
#     while queue:
#         current_word, count = queue.popleft()
        
#         if current_word == target:
#             return count
        
#         for i in range(len(words)):
#             if not visited[i]:
#                 diff_count = 0
#                 for a,b in zip(current_word, words[i]):
#                     if a!=b:
#                         diff_count +=1
#                 if diff_count == 1:
#                     visited[i] = True
#                     queue.append((words[i],count +1))
    
    
#     return 0

from collections import deque

def solution(begin, target, words):
    # 예외 처리: target이 words 안에 없으면 죽었다 깨어나도 못 바꿈
    if target not in words:
        return 0
    
    # 1. 큐 초기화 (현재 단어, 현재 단계 수)
    queue = deque([(begin, 0)])
    visited = [False] * len(words) # 방문 여부 체크 (무한 루프 방지)
    
    # 2. BFS 탐색 시작
    while queue:
        current_word, count = queue.popleft()
        
        # 타겟 단어에 도달했으면 단계 수(count) 반환 (최단 거리 보장)
        if current_word == target:
            return count
        
        # 3. words에 있는 단어들 중, 연결될 수 있는(알파벳 1개만 다른) 단어 찾기
        for i in range(len(words)):
            if not visited[i]:
                # 두 단어가 철자 하나만 다른지 확인하는 로직
                diff_count = 0
                for a, b in zip(current_word, words[i]):
                    if a != b:
                        diff_count += 1
                
                # 철자가 딱 1개만 다르면 -> 큐에 넣고 다음 탐색 후보로 등록
                if diff_count == 1:
                    visited[i] = True
                    queue.append((words[i], count + 1))
                    
    return 0