def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] >= 'a' and my_string[i] <='z':
            answer += my_string[i].upper()
        elif my_string[i] >= 'A' and my_string[i] <='Z':
            answer += my_string[i].lower()
    return answer