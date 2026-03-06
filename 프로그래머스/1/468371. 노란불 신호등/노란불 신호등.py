from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def is_yellow(t, G, Y, R):
    P = G + Y + R
    phase = (t - 1) % P
    return G <= phase < G + Y

def solution(signals):
    # signals: [(G,Y,R), ...]
    periods = [G+Y+R for G,Y,R in signals]
    
    # 기준 신호등: 노란불 구간이 짧거나(후보 적음), 주기가 짧은 걸로
    base = min(range(len(signals)), key=lambda i: (signals[i][1], periods[i]))
    G0, Y0, R0 = signals[base]
    P0 = G0 + Y0 + R0
    
    # 확실한 반복 상한: n<=5라 lcm을 계산해서 그 안에서 찾는 게 가장 명확
    # (문제 값이 크지 않으면 이게 제일 쉽고 안전)
    L = 1
    for p in periods:
        L = lcm(L, p)

    # base 신호등이 노란불인 시간만 후보로 검사
    # t-1 ≡ G0..G0+Y0-1 (mod P0)
    # 즉, 각 주기마다 Y0개의 후보만 보면 됨
    for start in range(1, L + 1, P0):
        # 이 주기에서 노란불인 구간: t = start+G0 .. start+G0+Y0-1
        # (t-1 기준이니까 t는 +1이 섞이는데, 아래처럼 쓰면 깔끔)
        base_start = start + G0
        base_end = start + G0 + Y0 - 1
        for t in range(base_start, min(base_end, L) + 1):
            ok = True
            for (G,Y,R) in signals:
                if not is_yellow(t, G, Y, R):
                    ok = False
                    break
            if ok:
                return t
    return -1