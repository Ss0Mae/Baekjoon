import math
def solution(n):
    answer = 0
    ans = int(math.sqrt(n))
    print(ans)
    if ans ** 2 == n:
        answer = (ans+1) ** 2
    else:
        answer = -1
    return answer