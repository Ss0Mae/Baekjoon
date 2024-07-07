def solution(board, k):
    # 결과를 저장할 변수
    result = 0
    
    # 2차원 배열의 행의 길이
    rows = len(board)
    # 2차원 배열의 열의 길이
    cols = len(board[0])
    
    # 배열을 순회하며 i + j <= k를 만족하는 원소들의 합을 구한다.
    for i in range(rows):
        for j in range(cols):
            if i + j <= k:
                result += board[i][j]
    
    return result