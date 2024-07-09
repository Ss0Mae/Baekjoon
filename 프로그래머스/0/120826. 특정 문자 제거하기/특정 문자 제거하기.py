def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] not in letter:
            answer+=my_string[i]
    return answer