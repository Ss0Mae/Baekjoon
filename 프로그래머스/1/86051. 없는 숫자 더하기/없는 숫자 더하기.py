def solution(numbers):
    ans = []
    for i in range(0,10,1):
        if i in numbers :
            pass
        else:
            ans.append(i)
    answer = sum(ans)
    return answer