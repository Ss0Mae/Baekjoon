def solution(sizes):
    max_w = 0
    max_h = 0
    for i in sizes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
    for i in sizes:
        if i[0] > max_w:
            max_w = i[0]
        if i[1] >max_h:
            max_h = i[1]
    max_solution = max_w * max_h
    return (max_solution)