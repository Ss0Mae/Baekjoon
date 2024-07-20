def solution(s):
    answer = False
    s= list(s)
    flag = 0
    lenCheck = True if len(s) == 4 or len(s) == 6 else False
    for i in s:
        if i.isalpha():
            flag = 1
    if flag ==0 and lenCheck == True: 
        answer = True
    
    return answer