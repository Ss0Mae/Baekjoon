#백트레킹, DFS?
def solution(k, dungeons):
   global visited, answer
   answer = 0 
   visited = [False for _ in range(len(dungeons))]
   dfs(k,0,dungeons)
   return answer

def dfs(k,cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = False