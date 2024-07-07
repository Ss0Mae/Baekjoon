def solution(arr):
    length = len(arr)
    answer = []
    for i in range(10):
        if (length == 2**i):
            return arr
        if (length >= 2**i and length < 2**(i+1)):
            tmp = 2**(i+1)
            break
    how = tmp - length
    for i in range(how):
        arr.append(0)
    return arr