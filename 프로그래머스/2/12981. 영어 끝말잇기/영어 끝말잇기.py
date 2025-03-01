def solution(n, words):
    # 첫 단어를 처리: 집합에 저장하고 마지막 글자 기록
    used_words = {words[0]}
    last_char = words[0][-1]
    
    # 두 번째 단어부터 처리
    for i, word in enumerate(words[1:], start=1):
        # 이미 사용된 단어거나 앞 단어의 마지막 글자와 맞지 않는 경우
        if word in used_words or word[0] != last_char:
            # 플레이어 번호와 몇 번째 차례인지를 계산하여 반환
            return [(i % n) + 1, (i // n) + 1]
        # 현재 단어를 사용된 단어 집합에 추가하고, 마지막 글자 업데이트
        used_words.add(word)
        last_char = word[-1]
    
    # 모든 단어가 규칙을 지킨 경우
    return [0, 0]
