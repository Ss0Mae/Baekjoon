def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    save = 0
    for l in lost:
        if l in reserve: # 잃어버린애가 여벌이 있으면 남은 체육복이 하나이기 때문에 수업을 들을수 있음
            save+=1
            reserve.remove(l)
            continue
        for r in reserve:
            if abs(l-r)<= 1 and (r not in lost):
                save+=1
                reserve.remove(r)
                break
    return (n-(len(lost)-save))