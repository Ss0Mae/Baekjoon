def solution(s):
    
    check = s.split(' ')
    
    for i in range(len(check)):
        check[i] = check[i].capitalize()
        
    return ' '.join(check)