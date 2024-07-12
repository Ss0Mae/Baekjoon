def solution(before, after):
    answer = 0
    cnt = 0
    for i in before:
        if before.count(str(i)) == after.count(str(i)):
            cnt +=1
    if cnt == len(before):
        answer =1
    answser = 0


    return answer
    