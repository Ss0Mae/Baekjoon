def solution(answers):
    # 1. 수포자 3인방의 찍기 패턴 하드코딩 (길이가 다 다름)
    pattern1 = [1, 2, 3, 4, 5]                  # 길이: 5
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]         # 길이: 8
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   # 길이: 10
    
    # 2. 각 수포자의 점수를 저장할 배열 [1번, 2번, 3번]
    scores = [0, 0, 0]
    
    # 3. 정답 배열(answers)을 순회하며 채점하기
    # enumerate를 쓰면 인덱스(i)와 정답(answer)을 동시에 뽑을 수 있어 매우 편리합니다.
    for i, answer in enumerate(answers):
        # 핵심 로직: 인덱스(i)를 각 패턴의 길이로 나눈 나머지(%)를 구하면
        # 패턴 배열의 범위를 벗어나지 않고 계속 순환하며(빙글빙글 돌며) 값을 꺼낼 수 있습니다.
        if answer == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            scores[2] += 1
            
    # 4. 가장 높은 점수 찾기
    max_score = max(scores)
    
    # 5. 최고 점수를 받은 사람 찾기
    result = []
    # scores 배열을 돌면서 최고 점수와 같은 점수를 가진 사람의 번호(인덱스 + 1)를 추가
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
            
    # 파이썬은 배열에 넣은 순서대로 유지되므로 이미 오름차순으로 정렬되어 있습니다.
    return result