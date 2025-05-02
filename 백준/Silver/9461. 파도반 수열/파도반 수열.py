import sys

T = int(sys.stdin.readline().strip())

# 파도반 수열 P(N)을 구하기 전에 필요한 숫자
nums = [1, 1, 1]

# N <= 100이므로 P(100)까지 정의
# P(1) -> P(0)으로 생각
# 따라서 P(0) ~ P(99)
# for문의 시작 지점을 정하면 끝지점은 실행 안 하므로 +1하여 100으로 설정
for i in range(3, 100):
    nums.append(nums[i-2] + nums[i-3])

# N에 맞게 출력
for _ in range(T):
    N = int(sys.stdin.readline().strip())

    print(nums[N-1])
