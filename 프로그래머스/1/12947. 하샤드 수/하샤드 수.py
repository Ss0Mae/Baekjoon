def solution(x):
    answer = True
    digit = 0
    tmp = x
    while(tmp>0):
        digit+=tmp%10
        tmp//=10
    if x % digit != 0: answer = False
    return answer