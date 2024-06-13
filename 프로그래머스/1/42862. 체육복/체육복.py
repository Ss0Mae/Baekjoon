def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    save = 0
    for l in lost:
        if l in reserve:
            save+=1
            reserve.remove(l)
            continue
        for r in reserve:
            if abs(l-r)<= 1 and (r not in lost):
                save+=1
                reserve.remove(r)
                break
    return (n-(len(lost)-save))