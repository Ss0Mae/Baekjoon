import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

def bfs():
    q = deque()
    count = 0 # 감염된 컴퓨터 수
    q.append(1) # 1번 컴퓨터로부터 시작
    visited[1] = True # 1번 컴퓨터 감염완료
    while q:
        cur = q.popleft()
        for i, val in enumerate(net[cur]): # 감염된 컴퓨터로부터 연결된 컴퓨터들에서
            if visited[val]==False: # 감염되지 않았다면
                q.append(val) # 감염리스트에 추가
                visited[val] = True # 감염완료
                count += 1 # 감염된 컴퓨터 수 1 증가
    print(count) # 모두 감염되었을 때 출력

visited = [False for _ in range(N+1)]
bfs()