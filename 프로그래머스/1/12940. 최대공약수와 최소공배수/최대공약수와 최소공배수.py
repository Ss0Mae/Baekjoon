import math
def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    answer.append(lcm(n,m))
    return answer