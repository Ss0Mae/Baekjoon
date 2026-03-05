from collections import defaultdict

def solution(gems):
    n = len(gems)
    K = len(set(gems))          # 전체 보석 종류 수

    count = defaultdict(int)
    have = 0                    # 현재 윈도우에 포함된 "종류 개수"
    best_l, best_r = 0, n - 1   # 0-index로 저장
    best_len = n                # 길이(= r-l)

    l = 0
    for r in range(n):
        # 오른쪽 확장
        if count[gems[r]] == 0:
            have += 1
        count[gems[r]] += 1

        # 모든 종류를 포함하면 왼쪽 줄이기
        while have == K and l <= r:
            # 답 갱신: 더 짧거나, 길이 같으면 시작이 더 앞이면
            if (r - l) < best_len:
                best_len = r - l
                best_l, best_r = l, r

            # l을 줄여보기
            count[gems[l]] -= 1
            if count[gems[l]] == 0:
                have -= 1
            l += 1

    # 문제는 1-based 인덱스로 반환
    return [best_l + 1, best_r + 1]