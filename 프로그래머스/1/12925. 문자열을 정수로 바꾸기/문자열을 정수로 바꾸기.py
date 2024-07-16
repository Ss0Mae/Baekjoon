def solution(s):
    answer = 0
    #s= list(s)
    if s[0] == '-':
        answer = int(s[1:]) * (-1)
    else:
        answer = int(s[:])
    return answer