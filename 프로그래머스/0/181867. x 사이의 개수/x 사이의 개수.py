def solution(myString):
    answer = []
    tot = 0
    for i in range(len(myString)):
        if myString[i] != 'x':
            tot += 1
        else:
            answer.append(tot)
            tot =0
    answer.append(tot)
    return answer