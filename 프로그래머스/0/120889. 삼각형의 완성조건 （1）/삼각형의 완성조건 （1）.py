def solution(sides):
    answer = 2
    maxSide = max(sides)
    if maxSide < sum(sides) - maxSide:
        answer = 1
    return answer