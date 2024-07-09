def solution(my_string):
    answer = ''
    com = ['a','e','i','o','u']
    for i in range(len(my_string)):
        if my_string[i] not in com:
            answer += my_string[i]
    return answer