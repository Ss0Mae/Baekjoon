def solution(n):
    mod = 1234567
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, (prev + curr) % mod
    return curr
