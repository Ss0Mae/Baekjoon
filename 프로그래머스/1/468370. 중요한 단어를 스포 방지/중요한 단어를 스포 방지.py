from collections import defaultdict

def solution(message, spoiler_ranges):
    # 1) 단어 분해: word + [l,r]
    words = []
    spans = []  # (l,r)
    n = len(message)

    i = 0
    while i < n:
        j = i
        while j < n and message[j] != ' ':
            j += 1
        words.append(message[i:j])
        spans.append((i, j-1))
        i = j + 1

    W = len(words)
    is_spoiler = [False] * W
    last_touch = [-1] * W  # 이 단어와 겹치는 spoiler_range 중 가장 큰 인덱스

    # 2) 투 포인터로 word-span과 spoiler_range 겹침 처리 (둘 다 오름차순)
    wi = 0
    for si, (s, e) in enumerate(spoiler_ranges):
        # 현재 스포 구간이 시작하기 전에 끝난 단어들 넘기기
        while wi < W and spans[wi][1] < s:
            wi += 1
        k = wi
        # 스포 구간과 겹치는 단어들 처리
        while k < W and spans[k][0] <= e:
            is_spoiler[k] = True
            last_touch[k] = max(last_touch[k], si)
            k += 1

    # 3) 비스포 영역에 등장한 단어 집합
    non_spoiler_seen = set()
    for idx, w in enumerate(words):
        if not is_spoiler[idx]:
            non_spoiler_seen.add(w)

    # 4) 클릭 시점별로 공개되는 단어 모으기
    reveal_buckets = defaultdict(list)  # click_idx -> [word_idx...]
    for idx in range(W):
        if is_spoiler[idx]:
            reveal_buckets[last_touch[idx]].append(idx)

    # 5) 클릭 순서대로 중요한 단어 카운트
    revealed_spoiler_words = set()
    ans = 0
    for click_idx in range(len(spoiler_ranges)):
        if click_idx not in reveal_buckets:
            continue
        for idx in reveal_buckets[click_idx]:  # idx 자체가 왼→오 순서
            w = words[idx]
            if w in non_spoiler_seen:
                continue
            if w in revealed_spoiler_words:
                continue
            ans += 1
            revealed_spoiler_words.add(w)

    return ans