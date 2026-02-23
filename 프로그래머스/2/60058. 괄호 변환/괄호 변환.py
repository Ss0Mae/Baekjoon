# [도구 1] "균형잡힌 괄호 문자열" u, v로 분리하는 함수
def split_uv(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
            
        # 열린 괄호와 닫힌 괄호의 개수가 같아지는 최초의 순간 분리
        if count == 0:
            return w[:i+1], w[i+1:]
    return "", ""

# [도구 2] "올바른 괄호 문자열"인지 판단하는 함수 (스택 활용)
def is_correct(u):
    stack = []
    for char in u:
        if char == '(':
            stack.append(char)
        else:
            # 스택이 비어있는데 닫힌 괄호가 나오면 올바르지 않음
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return ""
        
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u, v = split_uv(p)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
    if is_correct(u):
        # 3-1. 문자열 v에 대해 1단계부터 다시 수행한 결과를 u에 이어 붙여서 반환합니다.
        return u + solution(v)
        
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 4-2. 문자열 v에 대해 1단계부터 다시 수행한 결과 문자열을 이어 붙입니다.
        # 4-3. ')'를 다시 붙입니다.
        answer = '(' + solution(v) + ')'
        
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = u[1:-1] # 맨 앞과 맨 뒤 제거 (슬라이싱)
        for char in u:
            if char == '(':
                answer += ')'
            else:
                answer += '('
                
        # 4-5. 생성된 문자열을 반환합니다.
        return answer