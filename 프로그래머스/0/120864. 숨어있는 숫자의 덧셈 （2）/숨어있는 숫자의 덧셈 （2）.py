def solution(my_string):
    answer = 0
    tmp = 0
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            tmp += int(my_string[i])
            if (i+1) < len(my_string) and my_string[i+1].isdigit():
                tmp *= 10
            else:
                answer += tmp
                tmp = 0
    return answer