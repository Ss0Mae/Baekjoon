def solution(numbers, target):
    answer = 0
    
    # DFS를 수행할 내부 함수 정의
    # index: 현재 처리할 숫자의 인덱스
    # current_sum: 지금까지 더하거나 뺀 숫자들의 합계
    def dfs(index, current_sum):
        nonlocal answer # 바깥쪽 함수(solution)의 answer 변수를 수정하기 위해 선언
        
        # 1. 탈출 조건 (Base Case): 모든 숫자를 다 탐색했을 때
        if index == len(numbers):
            # 지금까지의 합계가 타겟 넘버와 같다면 카운트 증가
            if current_sum == target:
                answer += 1
            return # 탐색이 끝났으니 이전 가지로 돌아감 (백트래킹)
        
        # 2. 재귀 호출: 다음 숫자를 더하는 경우와 빼는 경우 두 갈래로 뻗어나감
        # 현재 인덱스의 숫자를 더하고, 다음 인덱스로 넘어감
        dfs(index + 1, current_sum + numbers[index])
        
        # 현재 인덱스의 숫자를 빼고, 다음 인덱스로 넘어감
        dfs(index + 1, current_sum - numbers[index])

    # 3. 탐색 시작: 0번째 인덱스부터, 합계 0인 상태로 시작
    dfs(0, 0)
    
    return answer