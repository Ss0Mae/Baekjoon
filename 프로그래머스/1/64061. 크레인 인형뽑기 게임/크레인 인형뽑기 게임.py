def solution(board, moves):
    answer = 0
    bucket = [] # 인형을 담을 바구니 (스택)
    
    # 1. 크레인 이동 명령 하나씩 처리
    for move in moves:
        col = move - 1 # 1번 위치는 인덱스 0번이므로 -1 처리
        
        # 2. 해당 열(col)에서 위에서부터 아래로 탐색 (행: row)
        for row in range(len(board)):
            # 2-1. 인형이 있다면 (0이 아니라면)
            if board[row][col] != 0:
                doll = board[row][col] # 인형 집기
                board[row][col] = 0    # 집었으니 빈 칸(0)으로 만듦
                
                # 3. 바구니 로직 (스택)
                # 바구니에 인형이 있고, 맨 위 인형이 지금 집은 거랑 같다면?
                if bucket and bucket[-1] == doll:
                    bucket.pop() # 터트림 (스택에서 제거)
                    answer += 2  # 인형 2개 사라짐 (점수 추가)
                else:
                    bucket.append(doll) # 바구니에 쌓기
                
                break # 인형을 하나 집었으면 해당 열 탐색 종료 (다음 move로)
                
    return answer