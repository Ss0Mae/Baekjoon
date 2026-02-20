def solution(m, n, board):
    # 파이썬의 문자열은 수정이 불가능(Immutable)하므로, 
    # 문자를 변경하기 쉽게 2차원 리스트로 변환하고 시작합니다.
    board = [list(row) for row in board]
    answer = 0
    #print(board)
    
    while True:
        # 1. 지워질 블록의 좌표를 담을 set (중복 제거 역할)
        matched = set()
        
        # 2x2를 확인해야 하므로 범위는 m-1, n-1까지입니다.
        for i in range(m - 1):
            for j in range(n - 1):
                # 현재 칸이 빈칸(0)이 아니고, 2x2 구역이 모두 같은 캐릭터라면
                if board[i][j] != 0 and \
                   board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    # 4개의 좌표를 모두 set에 추가합니다. (겹치는 좌표는 자동으로 1개만 남음)
                    matched.add((i, j))
                    matched.add((i, j+1))
                    matched.add((i+1, j))
                    matched.add((i+1, j+1))
                    
        # 2. 더 이상 지워질 블록이 없다면(set이 비어있다면) 게임 종료
        if not matched:
            break
            
        # 3. 블록 터트리기
        answer += len(matched) # 터지는 블록 개수 누적
        for i, j in matched:
            board[i][j] = 0    # 터진 자리를 빈칸(0)으로 표시
            
        # 4. 블록 떨어뜨리기 (중력 적용)
        # 세로줄(열, column) 단위로 하나씩 처리합니다.
        for j in range(n):
            # 해당 세로줄에서 0이 아닌 진짜 블록들만 순서대로 싹 모음 (위에서 아래 순서)
            valid_blocks = [board[i][j] for i in range(m) if board[i][j] != 0]
            
            # 모자란 길이만큼(원래 높이 m - 남은 블록 수) 0을 배열 앞(위쪽)에 채워줌
            empty_spaces = m - len(valid_blocks)
            new_column = [0] * empty_spaces + valid_blocks
            
            # 새로 만들어진 세로줄을 원래 보드에 덮어쓰기
            for i in range(m):
                board[i][j] = new_column[i]
                
    return answer