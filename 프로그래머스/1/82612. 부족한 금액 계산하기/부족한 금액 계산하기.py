def solution(price, money, count):
    answer = -1
    tot = 0
    for i in range(1, count+1):
        tot = tot + (price *i)
    if tot <= money:
        return 0
    else:
        return tot - money
