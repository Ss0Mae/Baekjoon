def solution(numbers):
    answer = 0
    numbers.sort()
    answer2 = numbers[0] * numbers[1]
    answer = numbers[len(numbers)- 1] *numbers[len(numbers)- 2]
    if abs(answer2) > abs(answer): answer = answer2
    return answer