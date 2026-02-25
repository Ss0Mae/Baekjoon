def solution(triangle):
    # 1. 꼭대기(0번째 줄)는 놔두고, 1번째 줄부터 맨 아랫줄까지 차례대로 내려옵니다.
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            
            # [Case 1] 현재 위치가 맨 왼쪽 끝인 경우
            # 내려올 수 있는 경로가 위층의 맨 왼쪽(j) 하나밖에 없음
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
                
            # [Case 2] 현재 위치가 맨 오른쪽 끝인 경우
            # 내려올 수 있는 경로가 위층의 맨 오른쪽(j-1) 하나밖에 없음
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
                
            # [Case 3] 현재 위치가 중간인 경우
            # 왼쪽 위(j-1)와 오른쪽 위(j) 두 곳에서 내려올 수 있으므로,
            # 둘 중 더 '큰 값'을 선택해서 현재 값과 더해줌 (DP의 핵심)
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    # 2. 맨 아랫줄(triangle[-1])까지 갱신이 끝났으므로, 
    # 맨 아랫줄에 저장된 누적 합들 중 가장 큰 값이 전체 경로의 최댓값이 됨
    return max(triangle[-1])