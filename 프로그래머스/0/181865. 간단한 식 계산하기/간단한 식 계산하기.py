def solution(binomial):
    answer = 0
    res = binomial.split()
    if res[1] == '+':
        answer = int(res[0]) + int(res[2])
    elif res[1] == '*':
        answer = int(res[0]) * int(res[2])
    elif res[1] == '-':
        answer = int(res[0]) - int(res[2])
    #print(res)
    #for i in range(len(binomial)):
        
    return answer