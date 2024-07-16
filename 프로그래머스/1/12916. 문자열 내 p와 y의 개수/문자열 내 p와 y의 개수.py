def solution(s):
    answer = False
    pcnt = 0
    ycnt = 0
    for i in s:
        if i == 'p' or i == 'P':
            pcnt+=1
        elif i == 'y' or i == 'Y':
            ycnt+=1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    if pcnt == ycnt:
        answer = True
    if pcnt == 0 and ycnt == 0: answer = True
    return answer