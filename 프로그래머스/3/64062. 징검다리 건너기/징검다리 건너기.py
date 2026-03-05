def solution(stones, k):
    # m명이 건널 수 있는지 판정
    def can_cross(m):
        cnt = 0  # 연속으로 못 밟는 돌 개수
        for s in stones:
            if s <= m:        # m명이 지나가면 0 이하가 되는 돌(=못 밟음)
                cnt += 1
                if cnt >= k:  # k개 연속이면 점프 한계로 실패
                    return False
            else:
                cnt = 0
        return True

    lo, hi = 0, max(stones)  # 0명~최대값까지
    while lo < hi:
        mid = (lo + hi + 1) // 2  # "최대 True" 찾기라 상향 mid
        if can_cross(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo +1