def solution(cipher, code):
    #idx = code-1
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0:
            answer+= cipher[i]
    return answer