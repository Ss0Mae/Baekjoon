def solution(box, n):
    answer = 0
    #answer += (box[0] // n * box[1] // n * box[2] // n)
    #answer = box[2] // n
    answer += (box[0] // n)
    answer *= (box[1] // n)
    answer *= (box[2] // n)
    return answer