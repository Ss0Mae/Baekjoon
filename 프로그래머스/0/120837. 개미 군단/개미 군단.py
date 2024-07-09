def solution(hp):
    answer = 0
    generalAnt = hp // 5
    hp = hp - generalAnt * 5
    soldierAnt = hp // 3
    hp = hp - soldierAnt * 3
    workerAnt = 0
    if hp != 0:
        workerAnt = hp // 1
    answer = generalAnt + soldierAnt + workerAnt
    return answer