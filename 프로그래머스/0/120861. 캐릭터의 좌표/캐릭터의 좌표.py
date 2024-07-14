def solution(keyinput, board):
    answer = []
    maxW = board[0]//2
    maxH = board[1] // 2
    wCnt = 0 
    hCnt = 0
    for oper in keyinput:
        if oper == 'left':
            if wCnt -1 >= maxW * (-1):
                wCnt-=1
        elif oper == 'right':
            if wCnt+1 <= maxW:
                wCnt+=1
        elif oper == 'up':
            if hCnt+1 <= maxH:
                hCnt +=1
        else:
            if hCnt - 1>= maxH * (-1):
                hCnt -= 1
    answer.append(wCnt)
    answer.append(hCnt)
    return answer