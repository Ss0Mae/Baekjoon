def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])
        a = a[2:].zfill(n) 
        # zfill(n) -> zfill()은 문자열 형태에서 지정한 길이만큼 0을 채워          줍니다.단, 지정한 길이는 기존 문자열의 길이를 포함합니다.
        #print(a)
        a = a.replace('1', '#').replace('0', ' ')
        answer.append(a)
    return answer
