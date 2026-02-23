def get_cds(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): # ★포인트1. 제곱근만큼만 반복
        if n%i == 0:
            if i == n//i: # 제곱근일 경우 -> 1개만 카운트하기
                cnt += 1
            else:
                cnt += 2 # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
        if cnt > limit:  # ★포인트2. 소수의 개수가 limit를 넘어가면
            return power #            강제로 power만큼을 return 
    return cnt

    
def solution(number, limit, power):
    total = 1
    for i in range(2, number+1):
        len_cds = get_cds(i, limit, power)
        total += len_cds

    return total
